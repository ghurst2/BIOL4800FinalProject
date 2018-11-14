#!/usr/bin/env python

class shortread:
	"""A class to store information about the short reads"""
#we could use this to store the first/last few nucleotides
	def __init__(self, StartNuc=" ", EndNuc=" "):
		self.StartNuc = StartNuc
		self.EndNuc = EndNuc
#this could be used to print them to the screen
	def ShortReadEnds(self):
		print("The first 10 nucleotides of the short read: %s" %(self.StartNuc))

		print("The last 10 nucleotides of the short read: %s" %(self.EndNuc))
#this could be used to show its location in a sequence ex. like it's the 3rd short read in the sequence.
class Find(shortread):
	"""A class to store information about the location of the short reads"""

	def __init__(self, Location=" ", StartNuc=" ", EndNuc=" "):
		shortread.__init__(self,StartNuc,EndNuc)
		self.Location = Location

	def search(self):
		print("This short read can be found at %s." %(self.Location))

ShortreadOne = Find(StartNuc= "AGCTGCAGAG", EndNuc = "GTATTCAGCA", Location = "Line three")

print(ShortreadOne.ShortReadEnds())
print(ShortreadOne.search())
