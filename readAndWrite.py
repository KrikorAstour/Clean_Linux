def main():
    beforeMIL_file = open("ubuntu22before.txt")
    afterMIL_file = open("afterMIL.txt")
    result = open("result.txt", "x")

    for after_line in afterMIL_file:
        found = False
        beforeMIL_file.seek(0) # move the file pointer to the beginning of the file
        for before_line in beforeMIL_file:
            if after_line.strip() == before_line.strip():
                found = True
                break
        if not found:
            result.write(after_line)

    beforeMIL_file.close()
    afterMIL_file.close()
    result.close()
    return 0
 ###########################################################################
  import mmap

def main():
    beforeMIL_file = open("ubuntu22before.txt", "r")
    afterMIL_file = open("afterMIL.txt", "r")
    result_file = open("result.txt", "w")

    # Memory map the files
    beforeMIL_map = mmap.mmap(beforeMIL_file.fileno(), 0, access=mmap.ACCESS_READ)
    afterMIL_map = mmap.mmap(afterMIL_file.fileno(), 0, access=mmap.ACCESS_READ)

    for line in afterMIL_map:
        if line not in beforeMIL_map:
            result_file.write(line)

    # Close the files
    beforeMIL_map.close()
    afterMIL_map.close()
    beforeMIL_file.close()
    afterMIL_file.close()
    result_file.close()

    return 0
  ############################################################################
  def main():
    beforeMIL_lines = set(open("ubuntu22before.txt").read().splitlines())
    afterMIL_lines = set(open("afterMIL.txt").read().splitlines())
    
    result = open("result.txt", "x")
    result.write('\n'.join(afterMIL_lines - beforeMIL_lines))
    
    return 0
