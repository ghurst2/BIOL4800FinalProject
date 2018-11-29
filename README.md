# BIOL4800FinalProject
The goal of our code is to assemble a DNA sequence from a list of DNA short reads.

How the program works:
The program uses commnand line argumets to read a file the contians a list of short reads. For every file in the command line argument the program reads the first line (shortread) in the file and defines it as a variable. Then the code will select the last 13bp (can be changed in the code) of the firstline and define it as the match sequence. Then the program reads all the other lines in the file and selects the first 13bp and defines it as a variable. If 
