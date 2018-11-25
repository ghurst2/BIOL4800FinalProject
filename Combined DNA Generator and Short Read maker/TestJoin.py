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

for each in range(1):
    dna = random_dna_sequence(300)
    f= open("GeneratedDNA.txt", "w+")
    print(dna, file=f)
    f.close()
    f= open("OrigionalStrand.txt", "w+")
    print(dna, file=f)
    f.close()

Value =int(input("Enter How Many Replica Strands You Want to Generate: "))
for x in range(Value):
    with open("GeneratedDNA.txt") as f_in, open("GeneratedDNA.txt", "a") as f_out :
        for row in f_in.readlines()[-1:] :
            f_out.write(row)
            f_out.close()

min_no_space = 55 #minimum length without spaces
max_no_space = 75 # max sequence length without space
no_space = 0
with open("GeneratedDNA.txt","r") as f, open("GeneratedShortReads.txt","w") as w: 
    for line in f:
        for c in line:
            w.write(c)
            if no_space > min_no_space:
                if random.randint(1,9) == 1 or no_space >= max_no_space:
                    w.write("\n")
                    no_space = 0
            else:
                no_space += 1
    f.close()
    w.close()
