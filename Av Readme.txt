Configuration Steps
1. Install the PyNamecheap library by running the following command in your terminal or command prompt:
pip install PyNamecheap

2. Update the credentials.py file with your Namecheap API credentials. Ensure that your IP address is correctly added to the whitelist in the Namecheap API settings. The credentials.py file should contain the following information:

3. Open the combinedFinal.py file and update the filename variable with the name of your CSV file containing domain information and required DNS values. Ensure that the CSV file is in the correct format and contains the necessary columns for the DNS records.

4. Run the script by executing the following command in your terminal or command prompt:
python dns_configuration.py

The script will generate API commands for configuring various DNS records and store them in the output_commands.txt file. It will then execute these API commands to add the DNS records to Namecheap. The execution results (stdout and stderr) will be logged in the output.txt file for your reference.

The CSV file should be in the format as you see in the example.csv file.


Note
Ensure you have valid Namecheap API credentials and appropriate permissions before running the script.
Review the CSV file for accurate data before executing the script to avoid unintended changes.
It is recommended to review the output.txt file after execution to check for any errors or issues during the DNS configuration process.