#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body

def readFile():
	inFile = open("words.txt")
	outFile = open("result.txt", "w")

	for line in inFile:
		if(len(line)>20):
			outFile.write(line)
	outFile.close()
	outFile = open("result.txt")
	print outFile.read()


##############################################################################
def main():
    readFile() # Call your functions here.

if __name__ == '__main__':
    main()
