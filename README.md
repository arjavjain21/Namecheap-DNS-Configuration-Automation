# Namecheap-DNS-Configuration-Automation

The "Namecheap DNS Configuration Automation Tool" is a Python script designed to automate the setup of various DNS records for domains using the Namecheap API. The script reads data from a CSV file containing domain information and generates API commands to configure DNS records, including Verification TXT, SPF, DMARC, DKIM, CTD CNAME, and Redirect Domain. The tool also executes these API commands to apply the DNS changes.

# Prerequisites:
- Python 3.x installed on the system.
- Namecheap API credentials with the necessary permissions to modify DNS records for the specified domains.
- namecheap-api-cli Python package installed. Install it using: pip install namecheap-api-cli.
- A CSV file (e.g., example.csv) containing the domain information and required DNS values for configuration in the required format (check example csv file).

# How it Works:
- Reading CSV Data: The script reads domain information and DNS records from the specified CSV file (justclose_sem_etc_w_dkim_value_added.csv) using the pandas library.
- Generating API Commands: For each domain in the CSV file, the script generates API commands for configuring various DNS records. It adds these commands to the output_commands.txt file, which includes commands for setting up Verification TXT, SPF, DMARC, DKIM, CTD CNAME, and Redirect Domain records.
- Applying DNS Changes: The script then executes the generated API commands from the output_commands.txt file, making use of the subprocess module. It applies the DNS changes in batches of 25 commands to avoid overwhelming the Namecheap API.
- Logging Results: The results of the API commands' execution (stdout and stderr) are logged in the output.txt file for reference.
- Data Updates: The script updates the CSV file with a 'done' status for each DNS record type, indicating that the record has been configured successfully.
- Opening Output: After completion, the script opens the output.txt file, allowing users to review the execution results.

# Handling Existing Records:

One notable feature of the script is its ability to detect and handle previously added DNS records for domains listed in the same CSV file. When the script is executed, it checks if any of the DNS records (e.g., Verification TXT, SPF, DMARC, DKIM, CTD CNAME, or Redirect Domain) already exist for a domain. This is achieved by examining the values in the xyz_done columns (e.g., verification_txt_value_done, dmarc_done, spf_done, dkim_value_done, ctd_cname_value_done, redirect_domain_done).

1. If a record is already present (indicated by "yes" in the respective xyz_done column), the script skips re-adding that specific DNS record for the domain. This ensures that existing records remain unchanged, and there is no duplication of DNS configurations for the same domain.
2. If a record is not present (indicated by "no" or an empty value in the xyz_done column), the script proceeds to add the DNS record using the corresponding API command.

# Usage:
Prepare your csv file with domain information and required DNS values.
Ensure that the namecheap-api-cli Python package is installed using pip install namecheap-api-cli.
Replace the filename variable with the actual CSV file name if different from the default one.
Run the script using python dns_configuration.py in the command-line.
The script will generate API commands in output_commands.txt, apply DNS changes, and log the results in output.txt.

# Important Notes:
Ensure you have valid Namecheap API credentials and appropriate permissions before running the script.
Review the CSV file for accurate data before executing the script to avoid unintended changes.
Adjust the limit variable to modify the batch size for executing the API commands as per your API rate limit and server capacity.

# Getting Started:
Clone or download the repository to your local machine.
Prepare your CSV file with domain information and required DNS values.
Install Python 3.x and the namecheap-api-cli package using pip.
Modify the filename variable in the script to match your CSV file name if different from the default.
Run the script using python dns_configuration.py in the command-line.

# Contributing:
If you wish to contribute to the project, please follow the guidelines outlined in the Contributing.md file. Fork the repository, make your changes, and submit a pull request for review.

# License:
This script is open-source and is provided under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

# Support:
If you encounter any issues or have questions regarding the script's usage, feel free to create an issue in the repository. The maintainers and the community will be glad to assist you.
