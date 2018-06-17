''' zCrack '''

# @ProgramName: zCrack
# @Author: Daniel Victor Freire Feitosa
# @Version: 1.0.0
# @License: Free Software GPL

''' Sorry bad english '''

import zipfile
from itertools import product
from threading import Thread
from os import _exit as exit
from sys import stdout, argv

def zCrack(filename, string, min_range, max_range): # Function to crack zip files

	zip_file = zipfile.ZipFile(filename) # Create handle of zip file
		
	for x in xrange(min_range, max_range): # Range of wordlists
		for xs in product(string, repeat=x): # Cartesian product
			passwd = ''.join(xs) # Password to test
			stdout.write('\r[-] Attemp password: {passwd}'.format(passwd=passwd)) # Print inline
			try:
				zipfile.extractall(pwd=passwd) # Try to extract zip file with password
				print '\n[+] Password found : {passwd} !\n'.format(passwd=passwd) # If worth print the password
				handle = open('passwd.txt', 'w') # Open the log archive to log password
				handle.write('\n[+] Password found : {passwd} !\n'.format(passwd=passwd)) # Write the same message of the crack
				handle.close() # Close the handler of log
				exit(0) # Exit all threads
			except:
				pass


if __name__ == '__main__':

	# Wordlist numerics
	numeric = '0123456789'
	numericReverse = numeric[::-1]

	# Wordlist alphabetical
	alphabet = 'abcdefghijklmnopqrstuvxzyw'
	alphabetUpper = alphabet.upper()
	alphabetReverse = alphabet[::-1]

	# Combinations
	alphabetNumeric = alphabet+numeric
	alphabetUpperNumeric = alphabetUpper+numeric

	# Combinations reverses
	alphabetNumericReverse = alphabetNumeric[::-1]
	alphabetUpperNumericReverse = alphabetNumericReverse[::-1]

	# All wordlists
	wordlists = [numeric, numericReverse, alphabet, alphabetUpper, alphabetReverse, alphabetNumeric, alphabetUpperNumeric, alphabetNumericReverse, alphabetUpperNumericReverse]

	# Args verify
	if len(argv) == 1:
		print '{scriptname} <zip_filename> <min_range> <max_range>'.format(scriptname=argv[0].split("\\")[len(argv[0].split("\\"))-1])
		exit(0)

	zip_filename = argv[1] # ZIP filename to crack
	min_range = int(argv[2]) # Min range to wordlists
	max_range = int(argv[3]) # Max range to wprdlists

	for wordlist in wordlists:
		Thread(target=zCrack, args=(zip_filename, wordlist, min_range, max_range,)).start() # Create the all threads
