#!/usr/bin/env python

import fileinput
import re

f = open("Test333.txt", "r")
print(f.read())

for x in range(50):
    with open("Test333.txt") as f_in, open("Test333.txt", "a") as f_out :
        for row in f_in.readlines()[-1:] :
            f_out.write(row)

#f= open("Test333.txt")
#for x, line in enumerate(f):
#    if x == 0:
#        print(line)
#f.close()
