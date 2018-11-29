# BIOL4800FinalProject
The goal of our code is to assemble a DNA sequence from a list of DNA short reads.

How the program works:
The program uses commnand line argumets to read a file the contians a list of short reads. For every file in the command line argument the program reads the first line (shortread) in the file and defines it as a variable. Then the code will select the last 13bp (can be changed in the code) of the firstline and define it as the match sequence. Then the program reads all the other lines in the file and selects the first 13bp and defines it as a variable. If 




Our code also gives you the option to generate random DNA to work with. Our code gereates a DNA strand that is 2000bp in length and saves that DNA strand to a new file for later comparison. The code then duplicates the DNA strand a number of times that the user chooses (and impunts in the command line), then it splits each line of DNA into 75 to 125bp length short reads. Once the code has generated the short reads, the code reads all lines that start with the same 13 characters and removes all of them but one. This will make sure that each line is unique so that the code will process faster and work more efficent.
