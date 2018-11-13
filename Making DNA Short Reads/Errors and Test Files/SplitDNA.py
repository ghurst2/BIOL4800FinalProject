#!/usr/bin/env python

import fileinput
import re

f = open("GeneratedDNA.txt", "a")
print(f.read())

f= open("GeneratedDNA.txt", "w+")
sed-i "backup"'s/(\w+)/$1^[ \t]+$1/g' DNAGEN.txt

