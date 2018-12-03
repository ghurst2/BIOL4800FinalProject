#!/usr/bin/env python

class contig(object):
	"""hold all short reads in contig"""
	def __init__(self,length):
#list to hold reads
		self.lists = []

#short reads generated in file are read in from file

file = open('shortread.txt', 'r')
lists = []
for reads in file.readlines():
	lists.append(reads)
lists[:] = [line.rstrip('\n') for line in lists]


class fragmentRecord(object):
	""" A class to define a short read within a contig."""
	def __init__(self,sequence):
		self.sequence = sequence

	def printRecord(self):
		print("Sequence: " +self.sequence)


Contig = contig(length="Length: ")

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
