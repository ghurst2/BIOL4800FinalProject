#!/usr/bin/env python

import fileinput

#open the file with the matched DNA short reads
#create a file with the modified version
f1 = open('CompleteDNAsequence.txt', 'r')
f2 = open('CompleteDNAsequence.txt.tmp', 'w')
for line in f1:
    f2.write(line.replace('_', '\n')) #replaces _ with tab
f1.close()
f2.close()

#opens modified file, reads first line and saves it to new file
lines = open('CompleteDNAsequence.txt.tmp').readlines()
open('ANSWER.txt', 'w').writelines(lines[:+1])
