import os.path
import logging
import platform
import subprocess
import sys

# The python version used to write this script
python_version = '3.10.6'

# These commands show if MIL is still installed on Ubuntu.
cmd_ubuntu_mil_full = 'dpkg-query -l |grep -E mil-full'
cmd_ubuntu_mil_lite = 'dpkg-query -l |grep -E mil-lite'

# These commands show if MIL is still installed on Redhat or Suse
cmd_rh_suse_mil_full = 'rpm -qa|grep -E mill-full'
cmd_rh_suse_mil_lite = 'rpm -qa|grep -E mill-lite'

formatter = logging.Formatter('%(asctime)s %(levelname)s | %(message)s')



def main():
	# Get the name of the linux distribution currently installed
	distro = getDistro()
	
	# Create logging files
	files_logger = setup_logger('first_logger', 'List of remaining MIL files.log')
	info_logger = setup_logger('second_logger', 'INFO.log')
	
	#Get the python version installed 
	python_current = platform.python_version()
	print(python_current)
	
	
	# Select the clean function that matches the distibution being used
	match distro:
		case "ubuntu":
			# Get the output of the commands to verify MIL is not installed
			check_ubuntu_mil_full = subprocess.getoutput(cmd_ubuntu_mil_full)
			check_ubuntu_mil_lite = subprocess.getoutput(cmd_ubuntu_mil_lite)
			
			# Check if MIL is still installed
			if check_ubuntu_mil_full == "" and check_ubuntu_mil_lite == "":
				print("MIL is not installed, we perform the check")
				cleanUbuntu(files_logger, info_logger)
				print("Terminus!")
			else:
				print("MIL is still installed on this device. Uninstall MIL in order to run this script.")
				cleanUbuntu(files_logger, info_logger)
		case "redhat":
			cleanRedhat()
		case "suse":
			cleanSuse()
		case _:
			print()
			#logger = logging.getLogger("cleanLinux.log")
			#logger.error('Could not recognize the linux distribution ==> ' + distro)
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
		info_logger = logging.getLogger()
		info_logger.error('Something went wrong in ' + METHOD_NAME)
			
	if 'ubuntu' in linux_distro.lower():
		return 'ubuntu'
	elif 'redhat' in linux_distro.lower():
		return 'redhat'
	elif 'suse' in linux_distro.lower():
		return 'suse'
	else:
		return 0


def cleanUbuntu(files_logger, info_logger):
# This function looks for all the file created by MIL in Ubuntu
	METHOD_NAME = 'cleanUbuntu Method'
	ubuntu_list_path = 'ubuntu/test.txt'
	filesFound = 0;
	valid_answer = False
	valid_confirm = False
	
	if(os.path.exists(ubuntu_list_path)):
		# Open the file that has all the list we need to check for Ubuntu
		with open(ubuntu_list_path) as f:
			for line in f:
				if(os.path.exists(line.strip())):
					filesFound += 1
					files_logger.info(line.strip())
		
		# If no files are found, delete the empty .log file								
		if(filesFound == 0):
			os.remove("List of remaining MIL files.log")
		info_logger.info(str(filesFound) + ' File(s) have been found')			
		
	else:	
		# If the list path does not exist, delete the empty .log file							
		os.remove("List of remaining MIL files.log")	
		info_logger.error('Path does not exist. ' + ubuntu_list_path + ' --- ' + METHOD_NAME)
		
	if(filesFound > 0):
		# Get input from user to delete the file if the answer is 'y' 'Y' 'yes' 'YES'
		while not valid_answer:
			answer = input(str(filesFound) + " File(s) are still on your PC, do you want to delete these files? (Y/N)\n")
			if answer.lower() == "y" or answer.lower() == "yes":
				valid_answer = True
				
				# Inner while loop to confirm the user answered yes before deleting everything
				while not valid_confirm:
					confirm = input("Are you sure you want to delete the files? (Y/N)\n")
					if confirm.lower() == "y" or confirm.lower() == "yes":
						# Tihs line executes the command below and it passes the ubuntu list path as an arg to the next script
						os.system('python3 runme.py ubunut ' + ubuntu_list_path)
						valid_confirm = True
					elif confirm.lower() == "n" or confirm.lower() == "no":
						valid_confirm = True
							
			elif answer.lower() == "n" or answer.lower() == "no":
				print("Answer was No")
				valid_answer = True

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

def setup_logger(name, log_file, level=logging.INFO):
    # This function helps setting up multiple log files

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
						
if __name__ == "__main__":
   main()
