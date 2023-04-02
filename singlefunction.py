import os
import platform

def cleanMILFiles(files_logger, info_logger):
    METHOD_NAME = 'cleanMILFiles'
    os_name = platform.system().lower()
    list_path = ''
    
    if os_name == 'linux':
        dist_name = platform.linux_distribution()[0].lower()
        if dist_name == 'ubuntu':
            list_path = 'ubuntu/test.txt'
            # Ubuntu-specific cleaning logic here
        elif dist_name == 'redhat':
            list_path = 'redhat/test.txt'
            # Redhat-specific cleaning logic here
        elif dist_name == 'suse':
            list_path = 'suse/test.txt'
            # Suse-specific cleaning logic here
        else:
            info_logger.error('Unsupported Linux distribution: %s' % dist_name)
            return
    else:
        info_logger.error('Unsupported operating system: %s' % os_name)
        return
    
    # Common code for all operating systems here
    filesFound = 0
    valid_answer = False
    valid_confirm = False

    if os.path.exists(list_path):
        with open(list_path) as f:
            for line in f:
                if os.path.exists(line.strip()):
                    filesFound += 1
                    files_logger.info(line.strip())

        if filesFound == 0:
            os.remove("List of remaining MIL files.log")
        info_logger.info(str(filesFound) + ' File(s) have been found')

    else:
        os.remove("List of remaining MIL files.log")
        info_logger.error('Path does not exist: %s --- %s' % (list_path, METHOD_NAME))

    if filesFound > 0:
        while not valid_answer:
            answer = input(str(filesFound) + " File(s) are still on your PC, do you want to delete these files? (Y/N)\n")
            if answer.lower() == "y" or answer.lower() == "yes":
                valid_answer = True

                while not valid_confirm:
                    confirm = input("Are you sure you want to delete the files? (Y/N)\n")
                    if confirm.lower() == "y" or confirm.lower() == "yes":
                        os.system('python3 runme.py %s %s' % (os_name, list_path))
                        valid_confirm = True
                    elif confirm.lower() == "n" or confirm.lower() == "no":
                        valid_confirm = True

            elif answer.lower() == "n" or answer.lower() == "no":
                print("Answer was No")
                valid_answer = True
