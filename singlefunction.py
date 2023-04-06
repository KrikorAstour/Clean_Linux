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
cmd_rh_suse_mil_full = 'sudo rpm -qa|grep -E mill-full'
cmd_rh_suse_mil_lite = 'sudo rpm -qa|grep -E mill-lite'

# The .log file formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s | %(message)s')

def main():
# The main function that will be executed once the script run	
	
	# Get the name of the linux distribution currently installed
	dist_name = getDistro()
	
	# Create logging files
	files_logger = setup_logger('first_logger', 'List of remaining MIL files.log')
	info_logger = setup_logger('second_logger', 'INFO.log')
	
	cleanMILFiles(files_logger, info_logger, dist_name)

def cleanMILFiles(files_logger, info_logger, dist_name):
# Verify MIL has been uninstalled correctly
    METHOD_NAME = 'cleanMILFiles'
    list_path = ''
        
    # Change the path of the list of MIL files based on the linux distribution in use
    if dist_name == 'ubuntu':
        list_path = 'ubuntu/test.txt'
        
    elif dist_name == 'redhat':
        list_path = 'redhat/test.txt'
        
    elif dist_name == 'suse':
        list_path = 'suse/test.txt'
        
    else:
    	
        info_logger.error('Unsupported Linux distribution: %s' % dist_name)
        return

    
    # Common code for all operating systems here
    filesFound = 0
    valid_answer = False
    valid_selection = False
    deleter_script = 'Deleter/deleter.py'
    
    if os.path.exists(list_path):
        with open(list_path) as f:
            for line in f:
                if os.path.exists(line.strip()):
                    filesFound += 1
                    files_logger.info(line.strip())
                    
            info_logger.info(str(filesFound) + ' File(s) have been found')
            
            print('\n' + str(filesFound) + " File(s) are still on your PC.\n")

    else:
        os.remove("List of remaining MIL files.log")
        info_logger.error('Path does not exist: %s --- %s' % (list_path, METHOD_NAME))
    
    # Ask the user what they want next   
    while not valid_selection:
    	print("Select an option and press Enter:")
    	selection = input("1) Display the list of the directories found.\n2) Delete the files created by MIL.\n3) Exit.\n\n")
    	
    	# Verify the selection is valid
    	if(selection != '1' and selection != '2' and selection != '3'):
    		print("\nInvalid selection.\n")
    	
    	elif(selection == '1'):
    		valid_selection = True
    		os.system('gedit ')
    		print("Deleting MIL files...")
    	
    	elif(selection == '2'):
    		valid_selection = True
    		os.system('python3 %s %s %s' % (deleter_script, dist_name, list_path))
    	
    	elif(selection == '3'):
    		valid_selection = True
    		sys.exit()
              
def getDistro():
	# This function gets the name of linux distribution and the version and returns it as a string
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
