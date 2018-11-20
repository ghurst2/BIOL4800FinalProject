#!/usr/bin/env python

FILE_NAME = "testprecomb.txt"
NR_MATCHING_CHARS = 13

lines = set()
output_lines = [] # keep track of lines you want to keep
with open(FILE_NAME, "r") as inF:
    for line in inF:
        line = line.strip()
        if line == "": continue
        beginOfSequence = line[:NR_MATCHING_CHARS]
        if not (beginOfSequence in lines):
            output_lines.append(line + '\n') # add line to list, newline needed since we will write to file
            lines.add(beginOfSequence)
print(output_lines)

with open(FILE_NAME, 'w') as f:
    f.writelines(output_lines) # write it out to the file
