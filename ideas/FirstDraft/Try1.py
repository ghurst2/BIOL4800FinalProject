#!/usr/bin/env python

class contig(object):
	"""hold all short reads in contig"""
	def  __init__(self):
		self.lists = []

file = open('shortread.txt', 'r')
self.lists = []
for reads in file.readlines():
	lists.append(reads)
self.lists[:] = [line.rstrip('\n') for line in self.lists]
print(self.lists)

class fragmentRecord(object):
	""" A class to define a short read within a contig."""
	def __init__(self,sequence,length):
		self.sequence = sequence
		self.length = len(sequence)

	def printRecord(self):
		print("Sequence: " +self.sequence)
		print("Length: " +self.length)

print("---shortreadinformation---")
for fragment in self.lists:
	fragment = fragmentRecord(sequence=fragment,length= len(fragment))
	fragment.printRecord()
	print()
