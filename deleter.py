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

	# Make sure the path exist and the file in not empty
	if os.path.exists(list_path):
        with open(list_path) as f:
            for line in f:
                if os.path.exists(line.strip()):
                    files_found += 1
                    files_logger.info(line.strip())
	
	# Creat a .log file to write down the deleted files
	delete_logger = setup_logger('delete_logger', 'Deleted files list.log')
	
	# Delete the files
	
	if files_found > 1:
		while not valid_answer:
			answer = input(str(files_found) + " File(s) are still on your PC, do you want to delete the file(s) ?(Y/N)")
			
			if answer.lower() == 'y' or answer.lower() == 'yes':
				valid_answer = True
				
				# Ask user for confirmation before deleting
				while not valid_confirm:
					confirm = input("Are you sure you want to delete the files? (Y/N)")
					
					if confirm.lower() == 'y' or confirm.lower() == 'yes'
						valid_confirm = True
						#delete here
					
					elif confirm.lower == 'n' or confirm.lower() == 'no'
						valid_confirm = True
						os.system('exit')
			
			else answer.lower() == 'n' or answer.lower() == 'no'
				valid_answer = True
				os.system('exit')
			
			with open(lis_path) as f:
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
	else:
		print('No files found')
		
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
