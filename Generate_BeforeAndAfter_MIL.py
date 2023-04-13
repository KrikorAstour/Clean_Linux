import subprocess
import os.path
import sys

# These commands show if MIL is still installed on Ubuntu.
cmd_ubuntu_mil_full = 'dpkg-query -l |grep -E mil-full'
cmd_ubuntu_mil_lite = 'dpkg-query -l |grep -E mil-lite'

# These commands show if MIL is still installed on Redhat or Suse
cmd_rh_suse_mil_full = 'sudo rpm -qa|grep -E mil-full'
cmd_rh_suse_mil_lite = 'sudo rpm -qa|grep -E mil-lite'

# These commands generate a text file with a list of files and directories
cmd_beforeMIL = 'sudo find / 2>/dev/null > beforeMIL.txt'
cmd_afterMIL = "sudo find / 2>/dev/null > afterMIL.txt"

# The .log file formatter
#formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s', "%Y-%m-%d %H:%M:S")

def main():

	distro = getDistro()
	
	if(isMILInstalled(distro)):
	

		# Make sure the file does not already exist to avoid duplicates
		if(os.path.isfile("/home/std/Documetns/afterMIL.txt")):
			print("The file already exists in the current directory.")
		else:
			
			os.system(cmd_afterMIL)
	else:
		
		if(os.path.isfile("/home/std/Documents/beforeMIL.txt")):
			print("The file already exists in the current directory.")
		else:
			
			os.system(cmd_beforeMIL)
			
		
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
		print("EX")
		#info_logger = logging.getLogger()
		#info_logger.error('Something went wrong in ' + METHOD_NAME)
			
	if 'ubuntu' in linux_distro.lower():
		return 'ubuntu'
	elif 'red hat' in linux_distro.lower():
		return 'redhat'
	elif 'suse' in linux_distro.lower():
		return 'suse'
	else:
		#info_logger.error('Error getting linux distribution in %s' % METHOD_NAME)
		return

def isMILInstalled(distro):
# Checks if MIL is still installed and returns a boolean
	
	METHOD_NAME = 'isMILInstalled Method'
	MIL_installed = True
	distro = str(distro)
	
	if distro.lower() == 'ubuntu':
		# Store the output of the command that shows if MIL packages on Ubuntu
		ubuntu_mil_full = subprocess.getoutput(cmd_ubuntu_mil_full)
		ubuntu_mil_lite = subprocess.getoutput(cmd_ubuntu_mil_lite)
		
		# If the output of the commands are empty, means MIL does not exist
		if ubuntu_mil_full == '' and ubuntu_mil_lite == '':
			MIL_installed = False
			return MIL_installed
			
		else:
			return MIL_installed
			
	elif distro.lower() == 'redhat' or distro.lower() == 'suse':
		rh_suse_mil_full = subprocess.getoutput(cmd_rh_suse_mil_full)
		rh_suse_mil_lite = subprocess.getoutput(cmd_rh_suse_mil_lite)
		
		if rh_suse_mil_full == '' and rh_suse_mil_lite == '':
			MIL_installed = False
			return MIL_installed
			
		else:
			return MIL_installed
				
	else:
		#info_logger.error('Error checking MIL installation %s' % METHOD_NAME)
		return

		
if __name__ == "__main__":
	main()
