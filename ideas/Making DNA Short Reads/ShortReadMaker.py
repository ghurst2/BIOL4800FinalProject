#!/usr/bin/env python

import random
min_no_space = 20
max_no_space = 60 # if max sequence length without space
no_space = 0
with open("GeneratedDNA.txt","r") as f, open("GeneratedShortReads.txt","w") as w: 
    for line in f:
        for c in line:
            w.write(c)
            if no_space > min_no_space:
                if random.randint(1,6) == 1 or no_space >= max_no_space:
                    w.write("\n")
                    no_space = 0
            else:
                no_space += 1
with open("GeneratedShortReads.txt") as k:
    print(k.read())
    f.close()
