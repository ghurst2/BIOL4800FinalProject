#!/usr/bin/env python

import fileinput
import re

Value =int(input("Enter How Many Replica Strands You Want to Generate: "))
for x in range(Value):
    with open("GeneratedDNA.txt") as f_in, open("GeneratedDNA.txt", "a") as f_out :
        for row in f_in.readlines()[-1:] :
            f_out.write(row)
