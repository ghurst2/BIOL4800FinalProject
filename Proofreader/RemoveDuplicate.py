#!/usr/bin/env python
#file name as variable
FILE_NAME = "GeneratedShortReads.txt"
#set matching characters limit
NR_MATCHING_CHARS = 13

lines = set()
output_lines = [] # keep track of lines you want to keep
#open the file with the short reads
with open(FILE_NAME, "r") as inF:
    for line in inF:
        line = line.strip()
        #sets if loop for the same 13 characters
        if line == "": continue
        beginOfSequence = line[:NR_MATCHING_CHARS]
        if not (beginOfSequence in lines):
            #moves line to be written to new file
            output_lines.append(line + '\n') # add line to list, newline needed since we will write to file
            lines.add(beginOfSequence)
            #prints the lines that you want to keep
print(output_lines)
with open(FILE_NAME, 'w') as f:
    f.writelines(output_lines) # write it out to the file
