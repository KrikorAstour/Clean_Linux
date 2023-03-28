import os.path
import logging


logging.basicConfig(filename='CleanLinux.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(levelname)s | %(message)s',
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
	linux_distro = ""
	osRelease = open('/etc/os-release')
	
	for line in osRelease:
		if 'pretty_name' in line.lower():
			linux_distro = line.split('=')[1]
			
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
	ubuntu_list_path = 'ubuntu/test.txt'
	filesDeleted = 0;
	try:
		with open(ubuntu_list_path) as f:
			for line in f:
				if(os.path.exists(line.strip())):
					os.remove(line.strip())
					filesDeleted += 1
			
	except:
		logger = logging.getLogger()
		logger.error('Something went wrong')
	

def cleanRedhat():
# This function deletes all the files created by MIL in RedHat
	redhat_list_path = 'redhat/test.txt'
	filesDeleted = 0
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
		logger.error('Something went wrong')
		print("Something went wrong opening", redhat_list_path)

# This function deletes all the files created by MIL in Suse		
def cleanSuse():
	suse_list_path = 'suse/test.txt'
	filesDeleted = 0
	try:
		with open(suse_list_path) as f:
			for line in f:
				if(os.path.exists(line.strip())):
					os.remove(line.strip())
					filesDeleted += 1

	except:
		print("Something went wrong opening", suse_list_path)

						
if __name__ == "__main__":
   main()
