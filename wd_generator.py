'''
	@Author : Daniel Victor Freire Feitosa
	@Version : 2.1.1
	@DanielFriere00
	YouTube : proxysec
	No-Copyrigths e pau no cu to temer :)
'''
from itertools import product
from os import system
from platform import uname
from sys import argv, exit, stdout
from time import strftime
from locale import setlocale, format, LC_NUMERIC

if uname()[0] == "Windows":
	system("color 0a && cls") # if windows
else:
	system("clear") # if linux
print ""
print "  _      _____    _____                      __          "
print "  | | /| / / _ \  / ___/__ ___  ___ _______ _/ /____  ____"
print "  | |/ |/ / // / / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/"
print "  |__/|__/____/  \___/\__/_//_/\__/_/  \_,_/\__/\___/_/   " 
print ""
print "	                                       by Daniel Freire"                                                                                                                                             


def file_stats(max_lenght):
	Fl = 7 ** max_lenght
	Fb = (max_lenght + 2) * Fl
	if Fb >= 1000 and Fb < 1000000:
		Fbfinal = Fb / 1000
		stdout.write("[+] Lines : %s\n[+] File size : %i Kb\n\n"%(Fl, Fbfinal))
	elif Fb >= 1000000 and Fb < 1000000000:
		Fbfinal = Fb / 1000000
	 	stdout.write("[+] Lines : %s\n[+] File size : %i Mb\n\n"%(Fl, Fbfinal))
	elif Fb >= 1000000000:
		setlocale(LC_NUMERIC, '')
		Fbfinal = Fb / 1000000000
		formato = format("%.*f", (0, Fbfinal), True)
		stdout.write("[+] Lines : %s\n[+] File size : "+formato+" Gb\n\n"%(Fl))
	else:
		stdout.write("[+] Lines : %s\n[+] File size : %i bytes\n\n"%(Fl))
	cmd = raw_input("[?] Do you want continue [Y/N] : ")
	if cmd == "N" or cmd == "n":
		exit()

def generator(min_lenght, max_lenght, chars, name):
	lines = 0
	try:
		file=open(name, "w")
	except IOError:
		print "\n[x] Error : %s este caminho nao existe\n"%(name)
		exit()
	file_stats(max_lenght)
	print ""
	for n in range(min_lenght, max_lenght + 1):
		for xs in product(chars, repeat=n):
			lines = lines + 1
			string=''.join(xs)
			file.write(string + "\n")
			stdout.write('\r[+] Saving character `%s`' % string)
			stdout.flush()
	print "\a"
	file.close()

def generator_param(min_lenght, max_lenght, chars, name, param, value):
	try:
		file=open(name, "w")
	except IOError:
		print "\n[x] Error : %s este caminho nao existe\n"%(name)
		exit()
	file_stats(max_lenght)
	print ""
	for n in range(min_lenght, max_lenght + 1):
		for xs in product(chars, repeat=n):
			string=''.join(xs)
			if param == "-pre":
				file.write(value+string + "\n")
			elif param == "-pos":
				file.write(string+value + "\n")
			else:
				return 1
			if param == "-pre":
				stdout.write('\r[+] Saving character `%s%s`'%(value,string))
			elif param == "-pos":
				stdout.write('\r[+] Saving character `%s%s`'%(string,value))
			stdout.flush()
	print "\a"
	file.close()

if len(argv)>=5:
	try:
		min_lenght=int(argv[1])
		max_lenght=int(argv[2])
		chars=argv[3]
		try:
			param=argv[5]
			try:
				value=argv[6]
			except IndexError:
				print "\n[-] Use wd_generator.py min_length max_length output_file -pre|-pos value"
				print "\n[-] Exemplo : wd_generator.py 4 4 wd.txt -pre proxy"
				print "   |-> Saida desse comando : proxy1234 ...\n"
				exit() 
			generator_param(min_lenght, max_lenght, chars, argv[4], param, value)
			print "\n[+] Wordlist created : " + argv[4]
			print ('\n[-] End time: %s' % strftime('%H:%M:%S'))
			exit()
		except IndexError:
			pass
		generator(min_lenght, max_lenght, chars, argv[4])
		print "\n[+] Wordlist created : " + argv[4]
		print ('\n[-] End time: %s' % strftime('%H:%M:%S'))
		exit()
	except KeyboardInterrupt:
		print "\n[x] Saindo ..."
else:
	print "\n[+] Simple usage : wd_generator.py min_length max_length string output_file\n"
	print "[+] With prefix or postfix : wd_generator.py min_length string output_file -pre|-pos value\n"
