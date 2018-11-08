#!/usr/bin/env python

#Allow for commandline arguments
import sys

#define the commandline arguments to a variable
FilesToRead = sys.argv
#remove program name,starting at value 1
listoffiles = FilesToRead[1:]
print(listoffiles)
#defining a function
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

def copy():
	"""This function is used to copy the contents of the users files into a new file"""
	for fil in listoffiles:
                userfile = open(fil,'r')
                userfile_contents = userfile.read()
                userfile.close()
                outfile = open('shortread.txt', 'w')
                outfile.write(userfile_contents)
                outfile.close()
	return

def firstmatch():
	"""Used to match the first line"""
	file = open('shortread.txt','r')
	firstline = file.readline()
#removes the last 5 nucleotides of the first line
	first = firstline[:-5]
#puts the first line(without the last 5 nuc.) from shortread.txt into a new file
	OutFileName = "CompleteDNAsequence.txt"
	outfile = open(OutFileName,'a')
	outfile.write("%s \n" %first)
#put the last bp of first line in a list
	Match_seq = []
	Match_nuc = firstline[-5:]
	Match_seq.append(Match_nuc)
#remove '\n' from the end of list
	Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
#Reads all lines in the file and matches lines with the match sequence
	for lines in file.readlines():
		otherlineStart = []
		otherline = lines[:4]
#puts the first 4 base pairs in a list
		otherlineStart.append(otherline)
		if otherlineStart == Match_seq:	#compares the first 4 bp of each line with the last 4 bp of first line
			print(lines)	#prints the line that it matches with
			matched = lines
#puts the matched line in a file
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %matched)
	return

def combine():
	"""This function used to combine two matched sequences"""
	OutFileName = "CompleteDNAsequence.txt"
	outfile = open(OutFileName,'r')
	filecontains = outfile.readlines()
#removes the end of line spaces(\n) and the empty values in the list
	filecontains[:] = [line.rstrip('\n') for line in filecontains]
	filecontains = filecontains[:-1]
	#joins the list values together and removes spaces (becomes a string?)
	joins = ''.join(filecontains)
	complete = joins.replace(" ","")
	#writes the new combined strand in the file.
	outfilew = open(OutFileName,'w')
	outfilew.write("%s \n" %complete)
	outoriginalfile = "shortread.txt"
	originalfile = open(outoriginalfile, 'r+')
#writes it at the top of the file
	originalfile.seek(0, 0)
	originalfile.write("%s" %complete)
	return

def match():
	"""This function will open a file and find a match at the end of the first line to the start of another line in the file."""
	file = open('shortread.txt','r')
	firstline = file.readline()
#removes the last 5 nucleotides of the first line ***MAYBE TRY TO MAKE IT CHANGE? OR USE INPUT()??***
	first = firstline[:-6]
#put the last bp of first line in a list
	Match_seq = []
	Match_nuc = firstline[-6:]
	Match_seq.append(Match_nuc)
#remove '\n' from the end of list
	Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
#Reads all lines in the file and matches lines with the match sequence
	for lines in file.readlines():
		otherlineStart = []
		otherline = lines[:5]
#puts the first 4 base pairs in a list
		otherlineStart.append(otherline)
		if otherlineStart == Match_seq:	#compares the first 4 bp of each line with the last 4 bp of first line
			print(lines)	#prints the line that it matches with
			matched = lines
			matchedtwo = matched[5:]
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %matchedtwo)
	return

#run the program
confirm()
for files in listoffiles:
	copy()
	firstmatch()
	combine()
	match()
	combine()
