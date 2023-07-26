import pandas as pd
import time
import subprocess
import os

filename='example.csv'
df = pd.read_csv(filename)

# Add 'done' columns for each record type to the input DataFrame
for record_type in ['verification_txt_value', 'dmarc', 'spf', 'dkim_value', 'ctd_cname_value', 'redirect_domain']:
    done_column = f'{record_type}_done'
    if done_column not in df.columns:
        df[done_column] = ''

with open('output_commands.txt', 'w') as f:
    for index, row in df.iterrows():
        domain = row['domain']
        
        # Verification TXT value
        if not pd.isnull(row['verification_txt_value']) and row['verification_txt_value_done'] != 'yes':
            address = row['verification_txt_value']
            command = f'python namecheap-api-cli --domain {domain} --add --type TXT --name @ --address "{address}" --ttl 3600\n'
            f.write(command)
            df.at[index, 'verification_txt_value_done'] = 'yes'
        
        # SPF value
        if row['spf_done'] != 'yes':
            command = f'python namecheap-api-cli --domain {domain} --add --type TXT --name @ --address "v=spf1 include:_spf.google.com ~all" --ttl 1800\n'
            f.write(command)
            df.at[index, 'spf_done'] = 'yes'
        
        # DMARC value
        if row['dmarc_done'] != 'yes':
            command = f'python namecheap-api-cli --domain {domain} --add --type TXT --name _dmarc --address "v=DMARC1; p=quarantine; rua=mailto:dmarc@hyperke.com; ruf=mailto:dmarc@hyperke.com; pct=90;" --ttl 1800\n'
            f.write(command)
            df.at[index, 'dmarc_done'] = 'yes'
        
        # DKIM value
        if not pd.isnull(row['dkim_value']) and row['dkim_value_done'] != 'yes':
            address = row['dkim_value']
            command = f'python namecheap-api-cli --domain {domain} --add --type TXT --name google._domainkey --address "{address}" --ttl 1800\n'
            f.write(command)
            df.at[index, 'dkim_value_done'] = 'yes'
        
        # CTD CNAME value
        if not pd.isnull(row['ctd_cname_value']) and row['ctd_cname_value_done'] != 'yes':
            ctd_cname_value = row['ctd_cname_value']
            command = f'python namecheap-api-cli --domain {domain} --add --type CNAME --name tracking --address "{ctd_cname_value}" --ttl 1800\n'
            f.write(command)
            df.at[index, 'ctd_cname_value_done'] = 'yes'
        
        # Redirect domain
        if not pd.isnull(row['redirect_domain']) and row['redirect_domain_done'] != 'yes':
            redirect_domain = row['redirect_domain']
            command = f'python namecheap-api-cli --domain {domain} --add --type URL --name @ --address "{redirect_domain}"\n'
            f.write(command)
            df.at[index, 'redirect_domain_done'] = 'yes'

# Save the updated DataFrame to the input CSV file
df.to_csv(filename, index=False)

# Show a statement that all CSV records were converted
print('All CSV records were converted.')
print('Executing commands.')

# Part 2: Execute the commands from the output_commands.txt file
with open('output_commands.txt', 'r') as f:
    commands = f.readlines()

limit = 25
with open('output.txt', 'w') as f:
    for i in range(0, len(commands), limit):
        batch = commands[i:i+limit]
        for command in batch:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            f.write(result.stdout.decode('utf-8'))
            f.write(result.stderr.decode('utf-8'))
        time.sleep(60)

print('Done. Opening output.txt')

ofname = 'output.txt'
open_command = f'open {ofname}' if os.name == 'posix' else f'start {ofname}'
os.system(open_command)