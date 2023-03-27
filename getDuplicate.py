import os.path
import logging
import platform
import distro
import sys
from os import path

def main():
	counter = 0
	with open('result.txt') as f:
		seen = set()
		for line in f:
			line_lower = line.lower()
			if line in seen:
				counter += 1
			else:
				seen.add(line_lower)
	print(counter)		
	return 0
	
if __name__ == "__main__":
	main()
