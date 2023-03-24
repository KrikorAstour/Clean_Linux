import os.path
import logging
import platform
import distro
import sys
from os import path

def main():

	afterMIL_lines = []
	beforeMIL_lines = []
		
	beforeMIL_file = open("ubuntu22before.txt")
	afterMIL_file = open("afterMIL.txt")
	result = open("result.txt", "x")
	beforeMIL = beforeMIL_file.readlines()
	afterMIL = afterMIL_file.readlines()
	
	#Read the file and store the values in a list
	for i in range(len(afterMIL)):
		afterMIL_lines.append(afterMIL[i].strip())
	
	#Read the file and store the values in a list
	for i in range(len(beforeMIL)):
		beforeMIL_lines.append(beforeMIL[i].strip())
	
	
	for i in range(len(afterMIL)):
		print(afterMIL[i])
		if afterMIL[i] in beforeMIL:
			continue
		else:
			result.write(afterMIL[i])
	
	
	beforeMIL_file.close()
	afterMIL_file.close()
	return 0
	
def getOSDetails(version):
	return version[4:11], version[12:18]		
if __name__ == "__main__":
   main()
