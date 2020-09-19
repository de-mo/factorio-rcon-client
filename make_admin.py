import factorio_rcon
import sys

print('Welcome to the script to make admin')

if len(sys.argv)<3:
	print("Connection information are missing")
	print('Enter hostname as first parameter and port as second parameter')
	sys.exit()

hostname = sys.argv[1]
port = sys.argv[2]

print('Connection to server ', hostname, ":", port)
print('Enter password: ', end = '')
pwd = input()

client = factorio_rcon.RCONClient(hostname, int(port), pwd)

print('Enter user to promote as admin: ', end = '')
usr = input()

cmd = "/promote " + usr

response = client.send_command(cmd)
print(response)
