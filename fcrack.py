#-*-coding: utf8-*-
'''
  Use com moderação, e adicione a hash que quiser, nocopyrigths, modifique !
  essa porra crackea o que você quiser, entenda o que ele ta fazendo e adicione
  mais hashs. flws vlws
'''
from hashlib import md5, sha1, sha512
from sys import argv, exit, stdout
from itertools import product
from os import system
from time import gmtime
from platform import uname

if uname()[0] == "Windows":
	system("cls")
else:
	system("clear")

print "    ____________                __  "
print "   / ____/ ____/________ ______/ /__"
print "  / /_  / /   / ___/ __ `/ ___/ //_/"
print " / __/ / /___/ /  / /_/ / /__/ ,<   "
print "/_/    \____/_/   \__,_/\___/_/|_|\n"                                  
print " @Author : Daniel Friere Feitosa"
print " @Version : 1.8.5"
print " @DanielFreire00"
print " {GitHub : https://github.com/proxyanon/}\n"
print "==================================================================================================\n"

def usage():
	print "[!] Uso : %s hash min_length max_length --chars=abcd OU --wordlist=wd_chars_min --type=md5|sha1|sha512"%(argv[0].split("\\")[len(argv[0].split("\\")) - 1])
	print "\n[-] Wordlists com strings"
	print " 1. wd_all => todas as senhas possiveis"
	print " 2. wd_chars => todas as senhas com letras possiveis"
	print " 3. wd_chars_min => todas as senhas com letras minusculas possiveis"
	print " 4. wd_chars_upper => todas as senhas com letras maiusculas possiveis"
	print "\n[-] Wordlists numericas e especiais"
	print " 1. wd_num => todas as senhas numericas possiveis"
	print " 2. wd_special => todas as senhas com caracteres especiais possiveis"
	print "\n[-] Wordlists combinadas"
	print " 1. wd_chars_min_num => todas as senhas com letras minusculas e numeros possiveis"
	print " 2. wd_chars_upper_num => todas as senhas com letras maiusculas e numeros possiveis"
	exit()

def run_wd(strhash, initial, final, wd, types):
	# gerar senhas
	starttime = gmtime()[5]
	wd_all = "0123456789abcdefghijklmnopqrstuvxzywABCDEFGHIJKLMNOPQRSTUVXZYW!@#$%&*()_-=+';:.,]}{[|^~º?"
	wd_num = "0123456789"
	wd_chars_min = "abcdefghijklmnopqrstuvxzyw"
	wd_chars_upper = "ABCDEFGHIJKLMNOPQRSTUVXZYW"
	wd_chars_all = "abcdefghijklmnopqrstuvxzywABCDEFGHIJKLMNOPQRSTUVXZYW"
	wd_chars_min_num = "abcdefghijklmnopqrstuvxzyw0123456789"
	wd_chars_upper_num = "ABCDEFGHIJKLMNOPQRSTUVXZYW0123456789"
	wd_special = "!@#$%&*()_-=+';:.,]}{[|^~º?"
	if wd == 1:
		wd = wd_all
	elif wd == "wd_num":
		wd = wd_num
	elif wd == "wd_chars_min":
		wd = wd_chars_min
	elif wd == "wd_chars_upper":
		wd = wd_chars_upper
	elif wd == "wd_chars":
		wd = wd_chars_all
	elif wd == "wd_chars_min_num":
		wd = wd_chars_min_num
	elif wd == "wd_chars_upper_num":
		wd = wd_chars_upper_num
	elif wd == "wd_special":
		wd = wd_special
	else:
		print "[-] Esta wordlist nao esta inclusa no script, talvez voce tenha que adiciona-la manualmente"
		exit()
	for n in range(initial, final + 1):
		for xs in product(wd, repeat=n):
			string=''.join(xs)
			if types == "md5" or types == "MD5":
				password = md5(string).hexdigest()
			elif types == "sha1" or types == "SHA1":
				password = sha1(string).hexdigest()
			elif types == "sha512" or types == "SHA512":
				password = sha512(string).hexdigest()
			else:
				print "[-] Este formato nao esta incluso no script, talvez voce tenha que fazer isso manualmente"
				exit()
			if strhash == password:
				final = gmtime()[5] - starttime
				print "\n[+] Crackeada => %s\n"%(string)
				print "[+] Duracao => %i segundos\n"%(final)
				print "\a"
				stdout.flush()
				exit()
			else:
				print "[-] Tentando => %s"%(string)
	final = gmtime()[5] - starttime
	print "\n[+] Duracao => %i secs\n"%(final)

def run_chars(strhash, initial, final, chars, types):
	starttime = gmtime()[5]
	for n in range(initial, final + 1):
		for xs in product(chars, repeat=n):
			string=''.join(xs)
			if types == "md5" or types == "MD5":
				password = md5(string).hexdigest()
			elif types == "sha1" or types == "SHA1":
				password = sha1(string).hexdigest()
			elif types == "sha512" or types == "SHA512":
				password = sha512(string).hexdigest()
			else:
				print "[-] Este formato nao esta incluso no script, talvez voce tenha que fazer isso manualmente"
				exit()
			if strhash == password:
				final = gmtime()[5] - starttime
				print "\n[+] Crackeada => %s\n"%(string)
				print "[+] Duracao => %i segundos\n"%(final)
				print "\a"
				stdout.flush()
				exit()
			else:
				print "[-] Tentando => %s"%(string)
	final = gmtime()[5] - starttime
	print "\n[+] Duracao => %i segundos\n"%(final)
try:
	if len(argv) < 6:
		usage()
	else:
		param = argv[4]
		types = argv[5].split("=")[1]
		check_param = argv[4].split("=")[0]
		if check_param == "--wordlist":
			arg = argv[4].split("=")[1]
			run_wd(argv[1], int(argv[2]), int(argv[3]), arg, types)
		elif check_param == "--chars":
			arg = argv[4].split("=")[1]
			run_chars(argv[1], int(argv[2]), int(argv[3]), arg, types)
		else:
			usage()
except KeyboardInterrupt:
	print "\n[x] Exiting ..."
	exit()
