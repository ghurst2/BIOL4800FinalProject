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

def strips():
	"""This function is used to put the last nucleotides into a list"""

	file = open('shortread.txt','r')
	firstline = file.readline()
	first = firstline[:-number]
	print(first)
#put the last bp of first line in a list
	Match_seq = []
	Match_seq.clear()
	Match_nuc = firstline[-number:]
	Match_seq.append(Match_nuc)
	print(Match_seq)
#remove '\n' from the end of list
	Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
	return

def combine():
	"""This Function is used to combine two strands in a file"""
	#reads the strands in the file
	OutFileName = "CompleteDNAsequence.txt"
	outfile = open(OutFileName,'r')
	filecontains = outfile.readlines()
	print(filecontains)
	#removes the end of line spaces(\n) and the empty values in the list
	filecontains[:] = [line.rstrip('\n') for line in filecontains]
	filecontains = filecontains[:-1]
	print(filecontains)
	#joins the list values together and removes spaces
	joins = ''.join(filecontains)
	complete = joins.replace(" ","")
	print(complete)
	#writes the new combined strand in the file.
	outfilew = open(OutFileName,'w')
	outfilew.write("%s \n" %complete)
	outoriginalfile = "shortread.txt"
	originalfile = open(outoriginalfile, 'r+')
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
			#print(lines)	#prints the line that it matches with
			matched = lines
			matchedtwo = matched[5:]
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %matchedtwo)
	return

#run the program
confirm()
number = 13
count = 0
for files in listoffiles:
	copy()
	file = open('shortread.txt','r')
	firstline = file.readline()
#removes the last 12 nucleotides of the first line
	first = firstline[:-number]
	print("This is the first line without the match seq")
	print(first)
#puts the first line(without the last 13 nuc.) from shortread.txt into a new file
	#OutFileName = "CompleteDNAsequence.txt"
	#outfile = open(OutFileName,'a')
	#outfile.write("%s \n" %first)
	#put the last bp of first line in a list
	Match_seq = []
	Match_nuc = firstline[-number:]
	Match_seq.append(Match_nuc)
	print("THis is the last bp of first line")
	print(Match_seq)
	#remove '\n' from the end of list
	Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
	for lines in file.readlines():
		otherlineStart = []
		otherline = lines[:number-1]
		print("this is the start of the other lines")
		print(otherline)
	#puts the first 4 base pairs in a list
		otherlineStart.append(otherline)
	#	print("first bp of all lines in file:")
	#	print(otherlineSt)
		if otherlineStart == Match_seq:
	#puts the first line without the matc seq/or last bp in the outfile
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %first)
			print(lines)
			matched = lines
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %matched)
			outfile.close()
			combine()
		else:
			while otherlineStart != Match_seq:	#compares the first 4 		bp of each line with the last 4 bp of first line
			#print("This line matches with the end of the first 		line/matchseq:")
				number = number - 1
				strips()
				count = count + 1
				print(count)
				break
			#print("happy")
				#if  otherlineStart == Match_seq:
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %first)
			print(lines)
			print(lines)	#prints the line that it matches with
			matched = lines
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %matched)
			outfile.close()
				#	combine()
			#break
			combine()

#	match()
#	combine()
#print("The complete DNA sequence can be found in the file \"CompleteDNASequence.txt\"")

