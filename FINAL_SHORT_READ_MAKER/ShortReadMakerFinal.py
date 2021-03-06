#!/usr/bin/env python

import sys
import numpy as NP
import fileinput
import re
import random

#Generate Random DNA Sequence

def random_dna_sequence(length):
	return ''.join(random.choice('ACTG') for each in range(length))
#DNA sequences with equal base probability
def base_frequency(dna):
	D = {}
	for base in 'ATCG':
		D[base] = dna.count(base)/float(len(dna))
	return D
#sets the length of the DNA strand and saves it to file
for each in range(1):
	dna = random_dna_sequence(3000)
	f= open("GeneratedDNA.txt", "w+")
	print(dna, file=f)
	f.close()
	f= open("OrigionalStrand.txt", "w+")
	print(dna, file=f)
	f.close()
#set how many replica strands (COMMAND LINE ARGUMENTS SHOULD BE 1 LESS THAN WHAT YOU WANT)
Value =int(input("Enter How Many Replica Strands You Want to Generate: "))
for x in range(Value):
	with open("GeneratedDNA.txt") as f_in, open("GeneratedDNA.txt", "a") as f_out :
		for row in f_in.readlines()[-1:] :
			f_out.write(row)
			f_out.close()
#sets sizes of Short reads
min_no_space = 75 #minimum length without
max_no_space = 120 # max sequence length without
no_space = 0
with open("GeneratedDNA.txt","r") as f, open("shortread.txt","w") as w: 
	for line in f:
		for c in line:
			w.write(c)
			#makes always true if loop
			if no_space > min_no_space:
				#randomizes numbers chosen for ==1
				if random.randint(1,10) == 1 or no_space >= max_no_space:
					w.write("\n")
					no_space = 0
			else:
				no_space += 1
	f.close()
	w.close()


#removes strands that start with the same 13 bp


#file name as variable
FILE_NAME = "shortread.txt"
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

with open(FILE_NAME, 'w') as f:
	f.writelines(output_lines) # write it out to the file
