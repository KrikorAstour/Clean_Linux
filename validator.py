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
cmd_rh_suse_mil_full = 'sudo rpm -qa|grep -E mil-full'
cmd_rh_suse_mil_lite = 'sudo rpm -qa|grep -E mil-lite'

# The .log file formatter
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s' , "%Y-%m-%d %H:%M:%S")

def main():
# The main function that will be executed once the script run	
	
	# Create logging files
	files_logger = setup_logger('first_logger', 'MIL_List.log')
	info_logger = setup_logger('second_logger', 'INFO.log')
	
	# Get the name of the linux distribution currently installed
	dist_name = getDistro(info_logger)
	
	# Check if MIL is deleted
	if (isMILDeleted(dist_name, info_logger)):
		cleanMILFiles(files_logger, info_logger, dist_name)
	
	else:
		print("MIL is still installed.")
	
def cleanMILFiles(files_logger, info_logger, dist_name):
# Verify MIL has been uninstalled correctly
    METHOD_NAME = 'cleanMILFiles'
    list_path = ''
        
    # Change the path of the list of MIL files based on the linux distribution in use
    if dist_name == 'ubuntu':
        list_path = 'Master_List/Master_list.txt'
    elif dist_name == 'redhat':
        list_path = 'redhat/list.txt'
        
    elif dist_name == 'suse':
        list_path = 'suse/result.txt'
        
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
        os.remove("MIL_List.log")
        print('Error occured. Check INFO.log for more information.')
        info_logger.error('Path does not exist: %s --- %s' % (list_path, METHOD_NAME))
        sys.exit()
    # Ask the user what they want next   
    while not valid_selection:
    	print("Select an option and press Enter:")
    	selection = input("1) Display the list of the directories found.\n2) Delete the files created by MIL.\n3) Exit.\n\n")
    	
    	# Verify the selection is valid
    	if(selection != '1' and selection != '2' and selection != '3'):
    		print("\nInvalid selection.\n")
    	
    	elif(selection == '1'):
    		valid_selection = True
    		subprocess.getoutput("gedit MIL_List.log")
    		sys.exit()
    	
    	elif(selection == '2'):
    		valid_selection = True
    		os.system('python3 %s %s %s' % (deleter_script, dist_name, list_path))
    	
    	elif(selection == '3'):
    		valid_selection = True
    		sys.exit()
              
def getDistro(info_logger):
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
	elif 'red hat' in linux_distro.lower():
		return 'redhat'
	elif 'suse' in linux_distro.lower():
		return 'suse'
	else:
		info_logger.error('Error getting linux distribution in %s' % METHOD_NAME)
		return
		
def isMILDeleted(distro, info_logger):
# Checks if MIL is still installed and returns a boolean
	
	METHOD_NAME = 'isMILDeleted Method'
	MIL_deleted = False
	distro = str(distro)
	
	if distro.lower() == 'ubuntu':
		# Store the output of the command that shows if MIL packages on Ubuntu
		ubuntu_mil_full = subprocess.getoutput(cmd_ubuntu_mil_full)
		ubuntu_mil_lite = subprocess.getoutput(cmd_ubuntu_mil_lite)
		
		# If the output of the commands are empty, means MIL does not exist
		if ubuntu_mil_full == '' and ubuntu_mil_lite == '':
			MIL_deleted = True
			return MIL_deleted
			
		else:
			return MIL_deleted
			
	elif distro.lower() == 'redhat' or distro.lower() == 'suse':
		rh_suse_mil_full = subprocess.getoutput(cmd_rh_suse_mil_full)
		rh_suse_mil_lite = subprocess.getoutput(cmd_rh_suse_mil_lite)
		
		if rh_suse_mil_full == '' and rh_suse_mil_lite == '':
			MIL_deleted = True
			return MIL_deleted
			
		else:
			return MIL_deleted
				
	else:
		info_logger.error('Error checking MIL installation %s' % METHOD_NAME)
		return
			
	

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
