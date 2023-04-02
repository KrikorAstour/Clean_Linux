import os

def cleanUbuntu(files_logger, info_logger):
    METHOD_NAME = 'cleanUbuntu Method'
    ubuntu_list_path = 'ubuntu/test.txt'
    filesFound = 0
    valid_answer = False
    valid_confirm = False

    try:
        if(os.path.exists(ubuntu_list_path)):
            with open(ubuntu_list_path) as f:
                for line in f:
                    if(os.path.exists(line.strip())):
                        filesFound += 1
                        files_logger.info(line.strip())
                        
            if(filesFound == 0):
                os.remove("List of remaining MIL files.log")
            info_logger.info(str(filesFound) + ' File(s) have been found')
            
        else:
            os.remove("List of remaining MIL files.log")
            raise Exception('Path does not exist: ' + ubuntu_list_path)
        
        if(filesFound > 0):
            while not valid_answer:
                answer = input(str(filesFound) + " File(s) are still on your PC, do you want to delete these files? (Y/N)\n")
                if answer.lower() == "y" or answer.lower() == "yes":
                    valid_answer = True
                    while not valid_confirm:
                        confirm = input("Are you sure you want to delete the files? (Y/N)\n")
                        if confirm.lower() == "y" or confirm.lower() == "yes":
                            try:
                                os.system('python3 runme.py ubunut ' + ubuntu_list_path)
                                valid_confirm = True
                            except Exception as e:
                                info_logger.error('Error deleting files: ' + str(e))
                                valid_confirm = True
                        elif confirm.lower() == "n" or confirm.lower() == "no":
                            valid_confirm = True
                elif answer.lower() == "n" or answer.lower() == "no":
                    print("Answer was No")
                    valid_answer = True
    except Exception as e:
        info_logger.error(str(e) + ' --- ' + METHOD_NAME)


import os

def cleanRedHat(files_logger, info_logger):
    # This function looks for all the files created by MIL in Red Hat
    METHOD_NAME = 'cleanRedHat Method'
    redhat_list_path = 'redhat/test.txt'
    filesFound = 0
    valid_answer = False
    valid_confirm = False
    
    if os.path.exists(redhat_list_path):
        # Open the file that has all the list we need to check for Red Hat
        with open(redhat_list_path) as f:
            for line in f:
                if os.path.exists(line.strip()):
                    filesFound += 1
                    files_logger.info(line.strip())
        
        # If no files are found, delete the empty .log file
        if filesFound == 0:
            os.remove("List of remaining MIL files.log")
        info_logger.info(str(filesFound) + ' File(s) have been found')
        
    else:
        # If the list path does not exist, log an error message and delete the empty .log file
        info_logger.error('Path does not exist: ' + redhat_list_path + ' --- ' + METHOD_NAME)
        os.remove("List of remaining MIL files.log")    
        return
    
    if filesFound > 0:
        # Get input from user to delete the file if the answer is 'y' 'Y' 'yes' 'YES'
        while not valid_answer:
            answer = input(str(filesFound) + " File(s) are still on your PC, do you want to delete these files? (Y/N)\n")
            if answer.lower() == "y" or answer.lower() == "yes":
                valid_answer = True
                
                # Inner while loop to confirm the user answered yes before deleting everything
                while not valid_confirm:
                    confirm = input("Are you sure you want to delete the files? (Y/N)\n")
                    if confirm.lower() == "y" or confirm.lower() == "yes":
                        # This line executes the command below and it passes the Red Hat list path as an arg to the next script
                        try:
                            os.system('python3 runme.py redhat ' + redhat_list_path)
                            valid_confirm = True
                        except Exception as e:
                            info_logger.error('Error deleting files: ' + str(e) + ' --- ' + METHOD_NAME)
                    elif confirm.lower() == "n" or confirm.lower() == "no":
                        valid_confirm = True
                            
            elif answer.lower() == "n" or answer.lower() == "no":
                print("Answer was No")
                valid_answer = True


                import os

def cleanSUSE(files_logger, info_logger):
    # This function looks for all the file created by MIL in SUSE Linux
    METHOD_NAME = 'cleanSUSE Method'
    suse_list_path = 'suse/test.txt'
    filesFound = 0
    valid_answer = False
    valid_confirm = False

    if os.path.exists(suse_list_path):
        # Open the file that has all the list we need to check for SUSE Linux
        with open(suse_list_path) as f:
            for line in f:
                if os.path.exists(line.strip()):
                    filesFound += 1
                    files_logger.info(line.strip())

        # If no files are found, delete the empty .log file
        if filesFound == 0:
            os.remove("List of remaining MIL files.log")
        info_logger.info(str(filesFound) + ' File(s) have been found')
    else:
        # If the list path does not exist, delete the empty .log file
        os.remove("List of remaining MIL files.log")
        info_logger.error('Path does not exist. ' + suse_list_path + ' --- ' + METHOD_NAME)

    if filesFound > 0:
        # Get input from user to delete the file if the answer is 'y' 'Y' 'yes' 'YES'
        while not valid_answer:
            answer = input(str(filesFound) + " File(s) are still on your PC, do you want to delete these files? (Y/N)\n")
            if answer.lower() == "y" or answer.lower() == "yes":
                valid_answer = True

                # Inner while loop to confirm the user answered yes before deleting everything
                while not valid_confirm:
                    confirm = input("Are you sure you want to delete the files? (Y/N)\n")
                    if confirm.lower() == "y" or confirm.lower() == "yes":
                        # This line executes the command below and it passes the SUSE list path as an arg to the next script
                        os.system('python3 runme.py suse ' + suse_list_path)
                        valid_confirm = True
                    elif confirm.lower() == "n" or confirm.lower() == "no":
                        valid_confirm = True

            elif answer.lower() == "n" or answer.lower() == "no":
                print("Answer was No")
                valid_answer = True

