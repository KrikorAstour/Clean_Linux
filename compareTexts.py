import os.path
import logging
import platform
import distro
import sys
from os import path

def main():
	lines = []
	beforeMIL_file = open("ubuntu22before.txt")
	afterMIL_file = open("afterMIL.txt")
	
	beforeMIL = beforeMIL_file.readlines()
	afterMIL = afterMIL_file.readlines()
	
	#Read the file and store the values in a list
	for i in range(len(afterMIL)):
		lines.append(afterMIL[i].strip())
	
	print(len(lines))
	
	
	str = '/opt/matrox_imaging/contexts/FCNET_MONO_XL.mclass'
	
	if str in lines:
		print("yes")
	else:
		print("nop")
	beforeMIL_file.close()
	afterMIL_file.close()
	return 0
	
def getOSDetails(version):
	return version[4:11], version[12:18]		
if __name__ == "__main__":
   main()
