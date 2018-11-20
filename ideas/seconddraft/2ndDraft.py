#!/usr/bin/env python

#Allow for commandline arguments
import sys

#define the commandline arguments to a variable
FilesToRead = sys.argv
#remove program name,starting at value 1
listoffiles = FilesToRead[1:]
print(listoffiles)
number = 13
#for files in command line open each file and read the firstline
for files in listoffiles:
	file = open(files, 'r')
	firstline = file.readline()
#create a variable for the first short read without the matching end
	first = firstline[:-number]
	print(first)
#create a variable for the matching end
	Match_seq = []
	Match_nuc = firstline[-number:]
	Match_seq.append(Match_nuc)
	Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
	print(Match_seq)
#reads the rest of the lines in the file and creates a variable for the first bp
	for restoflines in file.readlines():
		otherlineStart = []
		otherline = restoflines[:number-1]
		otherlineStart.append(otherline)
		print(otherlineStart)
#if match seq equals the other lines bp then it puts the first line and the matched line in a file
		if Match_seq == otherlineStart:
			print(restoflines)
			MatchedLine = restoflines
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %first)
			outfile.write("%s \n" %MatchedLine)
			outfile.close()
#removes the first line from the shortread file
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
				if i != MatchedLine:
					removefile.write(i)
			removefile.truncate()
			removefile.close()
#combines the 2 short reads that matched 
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'r')
			filecontains = outfile.readlines()
			print(filecontains)
			filecontains[:] = [line.rstrip('\n') for line in filecontains]
			filecontains = filecontains[:-1]
			print(filecontains)
			joins = ''.join(filecontains)
			complete = joins.replace(" ","")
			print(complete)
			outfile.close()
#outputs the matched seq back into the shortread file 
			outfilew = open(OutFileName,'w')
			outfilew.write("%s \n" %complete)
			outoriginalfile = "shortread.txt"
			originalfile = open(outoriginalfile, 'r+')
			lin = originalfile.readlines()
			originalfile.seek(0)
			originalfile.write("%s \n" %complete)
			for lined in lin:
				originalfile.write(lined)
			originalfile.close()
#if it doesnt match then does a while loop
		else:
			while Match_seq != otherlineStart:
#changes the value of number so will decrease the amount of ends it's looking for
				number = number - 1
				print(number)
				file = open('shortread.txt', 'r')
				firstline = file.readline()
				print(firstline)
#redefines what the match seq and otherline start is (wiht the new number)
				first = firstline[:-number]
				Match_seq.clear()
				Match_nuc = firstline[-number:]
				Match_seq.append(Match_nuc)
				Match_seq[:] = [line.rstrip('\n') for line in Match_seq]
				Match_seq = [x.strip(' ') for x in Match_nuc]
				Match_seq.pop()
				what = ''.join(Match_seq)
				Match_seq.clear()
				Match_seq.append(what)
				print(Match_seq)
				for restoflines in file.readlines():
					otherlineStart.clear()
					otherline = restoflines[:number-2]
					otherlineStart.append(otherline)
					otherlineStart[:] = [line.rstrip('\n') for line in otherlineStart]	
					print(otherlineStart)
					file.close()
			#if it does match it does the same thing as it did above 
#***we can put in funcitons later		
			print(restoflines)
			MatchedLine = restoflines
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'a')
			outfile.write("%s \n" %first)
			outfile.write("%s \n" %MatchedLine)
			outfile.close()
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
				if i != MatchedLine:
					removefile.write(i)
			removefile.truncate()
			removefile.close()
			OutFileName = "CompleteDNAsequence.txt"
			outfile = open(OutFileName,'r')
			filecontains = outfile.readlines()
			print(filecontains)
			filecontains[:] = [line.rstrip('\n') for line in filecontains]
			filecontains = filecontains[:-1]
			print(filecontains)
			joins = ''.join(filecontains)
			complete = joins.replace(" ","")
			print(complete)
			outfile.close()
			outfilew = open(OutFileName,'w')
			outfilew.write("%s \n" %complete)
			outoriginalfile = "shortread.txt"
			originalfile = open(outoriginalfile, 'r+')
			lin = originalfile.readlines()
			originalfile.seek(0)
			originalfile.write("%s \n" %complete)
			for lined in lin:
				originalfile.write(lined)
			originalfile.close()	
