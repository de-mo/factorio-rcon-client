import factorio_rcon
import sys

print('Welcome to the factorio RCON Client')

if len(sys.argv)<3:
	print("Connection information are missing")
	print('Enter hostname as first parameter and port as second parameter')
	sys.exit()

hostname = sys.argv[1]
port = sys.argv[2]

print('Connection to server ', hostname, ":", port)
print('Enter password: ', end = '')
pwd = input()

try:
	client = factorio_rcon.RCONClient(hostname, int(port), pwd)
except ConnectionError as err:
	print("Connection Error: {0}".format(err))
	sys.exit()

print("Connected to the server")
print("use !q to quit")

loop = True
lineprompt ="Factorio Server > "

while loop:
	print(lineprompt, end = '')
	cmd = input()
	if cmd == "!q":
		loop = False
		break
	else:
		response = client.send_command(cmd)
		print(response)

print("bye")
