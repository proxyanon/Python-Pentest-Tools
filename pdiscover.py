import sys, socket

def scan():
	if len(sys.argv) >= 2:
		print ""
		print "PortScanner por Daniel Freire"
		print "-----------------------------\r\n"
		for porta in range(21,8080):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			if s.connect_ex((sys.argv[1], porta)) == 0:
				print "	Porta",porta,"[Aberta]"
				s.close()
	else:
		print ""
		print "PortScanner por Daniel Freire"
		print "Exemplo : python pdiscover.py IP_SERVIDOR"

try:
	scan()
except KeyboardInterrupt:
	print ""
	print "[!] www.cookielooger.esy.es [!]"
	exit(0)
