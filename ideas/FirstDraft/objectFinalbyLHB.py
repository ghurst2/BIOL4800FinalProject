#!/usr/bin/env python

class contig(object):
	"""A class to define a contig in which a short read might reside."""
	def __init__(self,contigPosition,fragCount):
# names the contig according to its order in the final sequence
		self.contigPosition = contigPosition

# the number of total short reads in a contig
		self.fragCount = fragCount

# List to store sequence fragments in a contig.
		self.fragSequences = []


	def addFragment(self,newFragment):
		if newFragment not in self.fragSequences: #Only add fragments if they're not currently in list.
			self.fragSequences.append(newFragment)

# defining the variables used drafting the information found in an info-storage per short read.
	def printContigInfo(self):
		print(self.contigPosition + " includes the following short reads: ")
		for fragment in self.fragSequences:
			print(fragment)

# initiating a class to hold info on current individual short reads per contig, which can be retrieved for analyzing.

class fragmentRecord(object):
	"""This class is an example of a fragment record that holds individual short read info."""
	def __init__(self,fragment,length,gcContent,atContent):
		self.fragment = fragment
		self.length = length
		self.gcContent = gcContent
		self.atContent = atContent
		self.locations = [] #Add the contigs in which each individual short read resides.

# defines the command to print all information in association with a students record.

	def printRecord(self):
		print("Sequence: "+self.fragment)
		print("Length: "+self.length)
		print("GC-Content: "+self.gcContent)
		print("AT-Content: "+self.atContent)
		for course in self.locations:
			print("Located in: "+contig.contigPosition)

# Allows for a new contig to be added in the final sequence if not present.
	def addContig(self,contig):
		if contig not in self.locations:
			self.locations.append(contig)
# List of contigs available along with their info used to produce records.

Contig1 = contig(contigPosition="Contig1",fragCount="1")
Contig2 = contig(contigPosition="Contig2",fragCount="2")
Contig3 = contig(contigPosition="Contig3",fragCount="1")
 
# List of fragments and their associated information which is used to retain their information in records.

fragment1 = fragmentRecord(fragment="ATGGTACGTAGCGATCGATCGATG",length="24",gcContent="50%",atContent="50%")
fragment2 = fragmentRecord(fragment="GCGCGGCGCTA",length="12",gcContent="83.3%",atContent="16.6%")
fragment3 = fragmentRecord(fragment ="GCATGT",length="6",gcContent="50%",atContent="50%")

#ADDING FRAGMENTS TO THE CONTIGS
Contig1.addFragment(fragment1.fragment)
Contig2.addFragment(fragment2.fragment)
Contig2.addFragment(fragment3.fragment)
Contig3.addFragment(fragment3.fragment)

#adding a contig to each fragemnts info for fragmentRecord

fragment1.addContig(Contig1)
fragment2.addContig(Contig2)
fragment3.addContig(Contig2)
fragment3.addContig(Contig3)


# Ckeck Contigs
print("---Contig Information---")
for contig in [Contig1, Contig2, Contig3]:
	contig.printContigInfo()
	print()

#Check FragmentInfo
print("---Short Read Information---")
for fragment in [fragment1,fragment2,fragment3]:
	fragment.printRecord()
	print()

#LOCATION INFO, should be in fragment info ?

# position within each contig 
        #self.position = position        #"incorporate later"
# placement in sequence
        #self.fragNumber = fragNumber
# placement in sequence
        #self.fragNumber = fragNumber
#used in class: final sequence
# the number of contigs
#        self.contigCount

