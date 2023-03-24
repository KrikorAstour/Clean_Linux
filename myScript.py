import os.path
import logging
import platform
import distro
import sys
from os import path

def main():

	version, distro = getOSDetails(platform.version())
	print("Your distro is: ",distro , " Version: ", version)
	#with open("/etc/issue") as f:
	#     print(f.read().lower().split()[0])
	#print("File Exists: "+str(path.exists('MappStart.py')))
	#os.remove("test.py")
	arr = os.listdir("/home/std/Downloads")
	files = os.listdir("/home/std/Documents")
		
	for i in arr:
		print(i, "\n", end = '')
		if(i == "testtodelete"):
			#Removes directories
			os.rmdir(i)
			#Removes files
			os.remove(i)

	print("\n")	
	for i in files:
		print(i, "\n", end = '')

	#f = open("3-SysInfo64.txt", "r")
	#print(len(f.readlines()))

	logging.basicConfig(filename="logger.log", format='%(asctime)s %(message)s', filemode='w')
	logger=logging.getLogger()
	logger.setLevel(logging.DEBUG)

	logger.debug("This is the debug message")

	return 0

def getOSDetails(version):
	return version[4:11], version[12:18]		
if __name__ == "__main__":
   main()
