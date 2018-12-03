#!/usr/bin/env python

class contig(object):
	"""This class will hold all short reads within each contig, which is generated into seperate files"""
	def __init__(self):
#list to hold short reads per output file generated 
		self.lists = []

#short reads generated in ouput file are read in from file and appended to lists

file = open('shortread.txt', 'r')
lists = []
for reads in file.readlines():
	lists.append(reads)
lists[:] = [line.rstrip('\n') for line in lists]

#This class is to retain records on each fragment
class fragmentRecord(object):
	""" A class to define a short read within a contig."""
	def __init__(self,sequence):
		self.sequence = sequence

	def printRecord(self):
		print("Sequence: " +self.sequence)
		
#will now use printRecord def to apply info to fragmentRecord
#set fragment equal to generic version of input to avoid manual input
#use in for loop with list of short reads from class contig to obtain various types of information
#program specific loop to receieve data desired in return and create new variables of interest

print("---shortreadinformation---")
for fragment in lists:
	fragment = fragmentRecord(sequence=fragment)
	fragment.printRecord()
for fragment in lists:
	print("Length of: ",end='')
	print(fragment, end='')
	print(" is ",end='')
	print(len(fragment),end='')
	print( " base pairs.")
