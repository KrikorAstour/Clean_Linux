import os.path
import sys

def main():

	# Open and read the two text files
	if (os.path.isfile("beforeMIL.txt")):
		beforeMIL_lines = set(open("beforeMIL.txt").read().splitlines())
	else:
		print("beforeMIL.txt file does not exist in the current directory")
		
	if(os.path.isfile("afterMIL.txt")):
		afterMIL_lines = set(open("afterMIL.txt").read().splitlines())
	else:
		print("afterMIL.txt file does not exist in the current directory")
		sys.exit()
	# Create and open a new text file    
	if(os.path.isfile("Master_list.txt")):
		print("Master_list.txt already exists, delete the file and run the script again to generate new one.")
		sys.exit()
	else:
		result = open("Master_list.txt", "x")
	
	# Write the difference of the beforeMIL and afterMIL in the new text file
	result.write('\n'.join(afterMIL_lines - beforeMIL_lines))
	
	# Filter the lines, remove unnecessary lines
	with open("Master_list.txt", "r") as f:
		lines = f.readlines()
    
	with open("Master_list.txt", "w") as f:
		for line in lines:
			if(line.split('/')[1] != "proc" and line.split('/')[1] != "sys" and line.split('/')[1] != "dev" and "firefox" not in line.lower() and 'codemeter' not in line.lower() and 'dotnet' not in line.lower() and line.split('/')[1] != "tmp" and line.split('/')[1] != "run"):
				f.write(line)
    
	return 0
	
			
if __name__ == "__main__":
   main()
