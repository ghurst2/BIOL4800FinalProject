#!/usr/bin/env python

file = open('shortread.txt', 'r')
lists = []
for reads in file.readlines():
	lists.append(reads)
lists[:] = [line.rstrip('\n') for line in lists]
print(lists)
#for fragment in lists:
	#print("fragment length:")
	#print(len(fragment))

class fragment(object):
	""" A class to define a short read within a contig."""
	def __init__(self,sequence,length,gcContent):
		for fragment in lists:
			self.sequence = fragment
			self.length = len(fragment)
			self.gcContent = gcContent
	
	def printRecord(self):		
		for fragment in lists:
			print("Sequence: " +self.sequence)
			print("Length: " +self.length)
			print("GC-Content: "+self.gcContent)
print("---shortreadinformation---")
for fragment in lists:
	fragment.printRecord()
	print()
