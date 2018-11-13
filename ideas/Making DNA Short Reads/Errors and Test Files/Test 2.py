#!/usr/bin/env python

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
    print (dna)
