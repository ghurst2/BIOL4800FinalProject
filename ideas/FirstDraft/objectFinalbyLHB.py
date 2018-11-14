!#/usr/bin/env python

class shortreads(objects):
	"""A class to store the fragements created for sequencing."""
	def __init__(self):
	self.fragments = [] #List to store sequence fragments

	def addFragment(self,newFragment):
		if newFragment not in self.fragments: #Only add fragments if they're not currently in list.
			self.fragments.append(newFragment)

	def seperateFragments(self): 
