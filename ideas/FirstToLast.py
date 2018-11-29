#!/usr/bin/python


#Allow for commandline arguments
import sys

#define the commandline arguments to a variable
FilesToRead = sys.argv
#remove program name,starting at value 1
listoffiles = FilesToRead[1:]
print(listoffiles)
number = 13

def confirm():
	"""This function allows user to edit the list of files to be used in the program"""
	print("Are these the files you would like to use?")
	print("Press \"y\" key for Yes or press \"n\" key for No")
	useranswer = input()
#ensures user selects y or n
	while useranswer not in("y","n"):
		print("Please ensure you have selected either key: \"y\" or \"n\"")
		useranswer = input()
	if useranswer == "y":
#run the program
		print("files are correct")
	else:
		print("Would you like to remove or add files?")
		print("Press \"r\" to remove a file or press \"a\" to add a file")
		useranswer2 = input()
		while useranswer2 not in ("a","r"):
			print("Please ensure you have selected either key: \"a\" or \"r\"")
#removes the file a user selects from the listoffiles
			useranswer2 = input()
		if useranswer2 == "r":
			print("Enter the file you would like to remove")
			removefile = input()
			listoffiles.remove(removefile)
			print(listoffiles)
		else:
#adds a file the user inputs
			print("Enter the file you would like to add.")
			addfile = input()
			listoffiles.append(addfile)
			print(listoffiles)
	return listoffiles

#define the functions
def combine():
	"""This function is used to combine two short reads to make one"""
	OutFileName = "CompleteDNAsequence.txt"
	outfile = open(OutFileName,'r')
	filecontains = outfile.readlines()
	#print(filecontains)
	filecontains[:] = [line.rstrip('\n') for line in filecontains]	
	filecontains = filecontains[:-1]
	#print(filecontains)
	joins = ''.join(filecontains)
	complete = joins.replace(" ","")
	#print(complete)
	outfile.close()
	outfilew = open(OutFileName,'w')
	outfilew.write("%s \n" %complete)
	outoriginalfile = "shortread.txt"
	originalfile = open(outoriginalfile, 'r+')
	lin = originalfile.readlines()
	originalfile.seek(0)
	originalfile.write("%s\n" %complete)
	for lined in lin:
		originalfile.write(lined)
	originalfile.close()
	return

#run the program
confirm()
for files in listoffiles:
#	copy()
	#counts the number of shortreads/lines in the file
	num_lines = sum(1 for line in open('shortread.txt'))
	while num_lines != 1:
		#print(num_lines)
		if (num_lines == 1):
			break
		number = 14
		match = 'no'
		while match != 'yes':
			if match == 'yes':
				break
			number = number - 1
			#limits the number of bp matches to 4 bp. Inputs a '_' as a gap in the sequence
			if number == 3:
				#read first to last
				num_lines = sum(1 for line in open('shortread.txt'))
				while num_lines != 1:
				#print(num_lines)
				if (num_lines == 1):
					break
				number = :14
				match = 'no'
				while match != 'yes':
					if match == 'yes':
						break
					number = number + 1
				#adds a '_' to end of matchseq and outputs it and the next line to OutFileName.
				file = open('shortread.txt', 'r')
				firstline = file.readline()
				NoMatchLine = firstline.replace('\n','_')
				secondline = file.readline()
				file.close()
				OutFileName = "CompleteDNAsequence.txt"
				outfile = open(OutFileName,'w')
				outfile.write("%s \n" %NoMatchLine)
				outfile.write("%s \n" %secondline)
				outfile.close()
				#removes the NoMatchLine and secondline from the shortread file.
				removefile = open("shortread.txt", "r+")
				d = removefile.readlines()
				removefile.seek(0)
				for i in d:
					if i != firstline:
						removefile.write(i)
				removefile.truncate()
				removefile.close()
				removefile = open("shortread.txt", "r+")
				d = removefile.readlines()
				removefile.seek(0)
				for i in d:
					if i != secondline:
						removefile.write(i)
				removefile.truncate()
				removefile.close()
				#combines the lines in Complete and put it in shortread file
				combine()
				match = 'yes'
				num_lines = sum(1 for line in open("shortread.txt"))

			file = open(files, 'r')
			firstline = file.readline()
#	print("this is the firstline")
#	print(firstline)
#create a variable for the first short read without the matching end
			first = firstline[:-number]
#	print("THis is the firstline without matchseq")
#	print(first)
#create a variable for the matching seq
			Match_seq = []
			Match_nuc = firstline[-number:]
			Match_seq.append(Match_nuc)
			Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
	#		print("this is the match seq")
	#		print(Match_seq)
			#reads the rest of the lines in the file and creates a variable for the first bp
			for restoflines in file.readlines():
#		print("these are the other lines")
#		print(restoflines)
				otherlineStart = []
				otherline = restoflines[:number-1]
				otherlineStart.append(otherline)
				otherlineStart[:] = [line.rstrip('\n') for line in otherlineStart]
	#			print("this is the start of the other lines")
	#			print(otherlineStart)
#if the match_seq equals the otherlineStart it stops and outputs it to the CompleteDNAseq file
#also outputs the firstline without the match_seq to the file (to remove the overlap)
				if Match_seq == otherlineStart:
					if Match_seq != otherlineStart:
	#					print("no match")
						break
					matchLine = restoflines
	#				print(matchLine)
					OutFileName = "CompleteDNAsequence.txt"
					outfile = open(OutFileName,'w')
					outfile.write("%s \n" %first)
					outfile.write("%s \n" %matchLine)
					outfile.close()
#removes the firstline from the shortreads file
					removefile = open("shortread.txt", "r+")
					d = removefile.readlines()
					removefile.seek(0)
					for i in d:
						if i != firstline:
							removefile.write(i)
					removefile.truncate()
					removefile.close()
#removes the line that matched with the short reads file
					removefile = open("shortread.txt", "r+")
					d = removefile.readlines()
					removefile.seek(0)
					for i in d:
						if i != matchLine:
							removefile.write(i)
					removefile.truncate()
					removefile.close()
					combine()
					match = "yes"
					num_lines = sum(1 for line in open("shortread.txt"))
					break
	print("your complete DNA sequence can be found in CompleteDNAsequence.txt")
