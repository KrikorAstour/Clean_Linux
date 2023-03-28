import os.path
import logging


logging.basicConfig(filename='CleanLinux.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s | %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def main():
	
	distro = getDistro()
	
	match distro:
		case "ubuntu":
			cleanUbuntu()
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
# This function deletes all the file created by MIL in Ubuntu
	METHOD_NAME = 'cleanUbuntu Method'
	ubuntu_list_path = 'ubuntu/test.txt'
	filesDeleted = 0;
	
	if(os.path.exists(ubuntu_list_path)):
		try:
			with open(ubuntu_list_path) as f:
				for line in f:
					if(os.path.exists(line.strip())):
						os.remove(line.strip())
						filesDeleted += 1
			
			logger = logging.getLogger()
			logger.info(str(count) + ' Files have been deleted')			
				
		except:
			logger = logging.getLogger()
			logger.error('Something went wrong in ' + METHOD_NAME)
	else:
		logger = logging.getLogger()
		logger.error('Path does not exist. ' + ubuntu_list_path + ' --- ' + METHOD_NAME)
	

def cleanRedhat():
# This function deletes all the files created by MIL in RedHat
	METHOD_NAME = 'cleanRedhat Method'
	redhat_list_path = 'redhat/test.txt'
	filesDeleted = 0
	if(os.path.exists(redhat_list_path)):
		try:
			with open(redhat_list_path) as f:
				for line in f:
					if(os.path.exists(line.strip())):
						os.remove(line.strip())
						filesDeleted += 1
			logger = logging.getLogger()
			logger.info(str(count) + ' Files have been deleted')
		
		except:
			logger = logging.getLogger()
			logger.error('Something went wrong in ' + METHOD_NAME)
	else:
		logger = logging.getLogger()
		logger.error('Path does not exist. ' + redhat_list_path + ' --- ' + METHOD_NAME)	

		
def cleanSuse():
#This function deletes all the MIL files in Suse
	METHOD_NAME = 'cleanSuse Method'
	suse_list_path = 'suse/test.txt'
	filesDeleted = 0
	
	if(os.path.exists(suse_list_path)):
		try:
			with open(suse_list_path) as f:
				for line in f:
					if(os.path.exists(line.strip())):
						os.remove(line.strip())
						filesDeleted += 1
			
			logger = logging.getLogger()
			logger.info(str(count) + ' File(s) have been deleted')
		except:
			logger = logging.getLogger()
			logger.error('Something went wrong in ' + METHOD_NAME)
	else:
		logger = logging.getLogger()
		logger.error('Path does not exist. ' + suse_list_path + ' --- ' + METHOD_NAME)

						
if __name__ == "__main__":
   main()
