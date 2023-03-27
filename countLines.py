import os.path
import logging
import platform
import distro
import sys
from os import path

def main():
	
	afterMIL_lines = []
	beforeMIL_lines = []
		
	beforeMIL_file = open("before.txt")
	afterMIL_file = open("after.txt")
	result_file = open("result.txt")
	
	result = result_file.readlines()
	beforeMIL = beforeMIL_file.readlines()
	afterMIL = afterMIL_file.readlines()
	
	
	print(len(afterMIL))
	print(len(beforeMIL))
	print(len(result))
	print(781685 - 653852)
	print(len(afterMIL) - len(beforeMIL))
	beforeMIL_file.close()
	afterMIL_file.close()
	result_file.close()
	return 0
	
if __name__ == "__main__":
	main()
