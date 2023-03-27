import os.path
import logging
import platform
import distro
import sys

def main():
	counter = 0
	counter2 = 0
	with open('result.txt') as f:
		for line in f:
			if(os.path.exists(line.strip())):
				counter += 1
			else:
				counter2 +=1
	
	print("Files exist: ", counter)
	print("Files does not exist: ", counter2)
	print(471706 - 427651)
	return 0
	
def getOSDetails(version):
	return version[4:11], version[12:18]		
if __name__ == "__main__":
   main()
