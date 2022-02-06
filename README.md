# sshb
SSH Brute Force Attack in Python

Simple script for use when doing a Brute Force attck on SSH.  Simply run the script with the required arguments and run.  Will output a successful logon to a file so you don't have to run the script again if you misplace the correct credentials.

Grab the git repo:
`git clone https://github.com/jeffvader84/sshb`

Install the required python packages:
`pip install -r requirements.txt`

To use run:
`python3 sshb.py -t <IP> -u <Username> -p <password list file>`

If you need any additional help run the following command:
`python3 sshb.py -h`
