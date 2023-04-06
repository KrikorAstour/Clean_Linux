with open("l.log", "r") as f:
	lines = f.readlines()
    
with open("list.txt", "w") as f:
	for line in lines:
		if(line.split('/')[1] != "proc" and line.split('/')[1] != "sys" and line.split('/')[1] != "dev" and "/home/std/snap/firefox/" not in line and "codemeter" not in line and line.split('/')[1] != "tmp" and line.split('/')[1] != "run"):
			f.write(line)
