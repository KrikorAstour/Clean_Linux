import os.path
import logging
import platform
import distro
import sys
from os import path

def main():

	#Open and read the two text files
	beforeMIL_lines = set(open("before.txt").read().splitlines())
	afterMIL_lines = set(open("after.txt").read().splitlines())
	
	#Create and open a new test file    
	result = open("result.txt", "x")
	
	#Write the difference in the new text file
	result.write('\n'.join(afterMIL_lines - beforeMIL_lines))
    
	return 0
		

def getOSDetails(version):
	return version[4:11], version[12:18]		
if __name__ == "__main__":
   main()
