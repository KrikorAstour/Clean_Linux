import os.path
import logging
import platform
import subprocess

THE_PYTHON_VERSION_USED_TO_WRITE_THIS_SCRIPT = '3.10.6'

# These commands show if MIL is still installed on the device, if they returned empty, then mil is uninstalled so do the check/clean function
cmd_ubuntu_mil_full = 'dpkg-query -l |grep -E mil-full'
cmd_ubuntu_mil_lite = 'dpkg-query -l |grep -E mil-lite'

logging.basicConfig(filename='CleanLinux.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s | %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def main():
	# Get the name of the linux distribution currently installed
	distro = getDistro()

	#Get the python version installed 
	python_version = platform.python_version()
	print(python_version)
	
	# Check if MIL is still installed on Ubuntu
	check_ubuntu_mil_full = subprocess.getoutput(cmd_ubuntu_mil_full)
	check_ubuntu_mil_lite = subprocess.getoutput(cmd_ubuntu_mil_lite)
	
	
	# Select the clean function that matches the distibution
	match distro:
		case "ubuntu":
			if check_ubuntu_mil_full == "" and check_ubuntu_mil_lite == "":
				print("mil is not installed, we perform the check")
				cleanUbuntu()
			else:
				print("MIL is still installed on this device. Uninstall MIL then run this script.")
		case "redhat":
			cleanRedhat()
		case "suse":
			cleanSuse()
		case _:
			logger = logging.getLogger()
			logger.error('Could not recognize the linux distribution ==> ' + distro)
	return 0
	
def getDistro():
# This function gets the name of linux distribution and the version and retruns it as a string
	METHOD_NAME = 'getDistro Method'
	linux_distro = ""
	osRelease = open('/etc/os-release')
	
	try:
		for line in osRelease:
			if 'pretty_name' in line.lower():
				linux_distro = line.split('=')[1]
	except:
		logger = logging.getLogger()
		logger.error('Something went wrong in ' + METHOD_NAME)
			
	if 'ubuntu' in linux_distro.lower():
		return 'ubuntu'
	elif 'redhat' in linux_distro.lower():
		return 'redhat'
	elif 'suse' in linux_distro.lower():
		return 'suse'
	else:
		return 0


def cleanUbuntu():
# This function looks for all the file created by MIL in Ubuntu
	METHOD_NAME = 'cleanUbuntu Method'
	ubuntu_list_path = 'ubuntu/test.txt'
	filesFound = 0;
	
	if(os.path.exists(ubuntu_list_path)):
		
		with open(ubuntu_list_path) as f:
			for line in f:
				if(os.path.exists(line.strip())):
					filesFound += 1
		
		
		logger = logging.getLogger()
		logger.info(str(filesFound) + ' File(s) have been found')				
		
	else:
		logger = logging.getLogger()
		logger.error('Path does not exist. ' + ubuntu_list_path + ' --- ' + METHOD_NAME)
	

def cleanRedhat():
# This function looks for all the files created by MIL in RedHat
	METHOD_NAME = 'cleanRedhat Method'
	redhat_list_path = 'redhat/test.txt'
	filesFound = 0
	if(os.path.exists(redhat_list_path)):
		
		with open(redhat_list_path) as f:
			for line in f:
				if(os.path.exists(line.strip())):
					filesFound += 1
		logger = logging.getLogger()
		logger.info(str(filesFound) + ' File(s) have been found')

	else:
		logger = logging.getLogger()
		logger.error('Path does not exist. ' + redhat_list_path + ' --- ' + METHOD_NAME)	

		
def cleanSuse():
#This function looks for all the MIL files in Suse
	METHOD_NAME = 'cleanSuse Method'
	suse_list_path = 'suse/test.txt'
	filesFound = 0
	
	if(os.path.exists(suse_list_path)):
		try:
			with open(suse_list_path) as f:
				for line in f:
					if(os.path.exists(line.strip())):
						os.remove(line.strip())
						filesFound += 1
			
			logger = logging.getLogger()
			logger.info(str(filesFound) + ' File(s) have been found')
		except:
			logger = logging.getLogger()
			logger.error('Something went wrong in ' + METHOD_NAME)
	else:
		logger = logging.getLogger()
		logger.error('Path does not exist. ' + suse_list_path + ' --- ' + METHOD_NAME)

						
if __name__ == "__main__":
   main()
