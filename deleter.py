import sys
import os.path
import logging

# Get the linux distrubution passed argument from linumxscript.py
distro = sys.argv[1]

# Get the .txt file location that contains the files you want to delete from the linuxscript.py
list_path = sys.argv[2]


# The .log file formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s | %(message)s')

def main():
	files_found = 0
	deleted_files = 0
	valid_answer = False
	valid_confirm = False

	
	# Creat a .log file to write down the deleted files
	delete_logger = setup_logger('delete_logger', 'Deleted files list.log')
	
		# Ask user for confirmation before deleting
	while not valid_confirm:
		confirm = input("\nAre you sure you want to delete the files? (Y/N)")
		
		if confirm.lower() == 'y' or confirm.lower() == 'yes':
			valid_confirm = True
			
			# Read the .txt file and delete all existed files and directories
			with open(list_path) as f:
				for line in f:
					if(os.path.exists(line.strip())):
						if(os.path.isfile(line.strip())):
							os.remove(line.strip())
						else:
							os.system("sudo rm -r " + line.strip())
							#os.rmdir(line.strip())
							deleted_files += 1
							delete_logger.info(line)
							
			print(str(deleted_files) + ' File(s) have been deleted successfully.')
		
		elif confirm.lower() == 'n' or confirm.lower() == 'no':
			valid_confirm = True
			os.system('exit')
			
		

		
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
