# BIOL4800FinalProject
The goal of our code is to assemble a DNA sequence from a list of DNA short reads.

How the program works:

Our code gereates a DNA strand that is 3000bp (can be changed in the code) in length and saves that DNA strand to a new file for later comparison. The code then duplicates the DNA strand a number of times that the user chooses, then it splits each line of DNA into 75 to 125bp length short reads. Once the code has generated the short reads, the code reads all lines that start with the same 13 characters and removes all of them but one. This will make sure that each line is unique so that the code will process faster and work more efficent.

The program uses command line arguments to read a file the contains a list of short reads. For every file in the command line argument the program reads the first line (first short read) in the file and defines it as a variable. Then the code will select the last 13bp (can be changed in the code) of the first line and defines it as the match sequence. The program also defines the first line without the match sequence as a varibale (called first).Then the program reads all the other lines in the file and for each line it selects the first 13bp and defines it as a variable (otherlinestart). If the match sequence matches the start of one of the short reads then both the first line and the other short read that matched it is deleted from the short read file and then put into another file called CompleteDNAsequence.txt (the first line without the match sequence (variable name first) is put into the CompleteDNAsequence file to remove the overlap). The program then combines the two short reads into one DNA sequence. That complete sequence is then put back into top of the short read file. The program then repeates for each short read in the file. 
If a match is not found using 13bp the program will reduce by one until a match is found (12bp,11bp, etc.) or the minimum bp overlap is reached (minium overlap set to 8bp- can be changed in the code). If the program reaches the minimum overlap the program then starts over however, this time the program defines the match sequence as the first 13bp of the first line instead of the last and the last 13bp of the other line as (otherlineEnd). If the minimum overlap is reached again and there are still other short reads in the file. The program will input an underscore (_) as a gap and the program will continue to try to find matches until there is only one line in the shortread file.


How to run the program:
Run the python file (Final.py) and the file name that contains your short reads ('shortread.txt')



Example:

1. open terminal
2. give permissions to Final.py
3. run Final.py "./Final.py shortread.txt"
4. Follow prompts and enter in vlaues
5. select yes if "shortread.txt" is the selected file and no if "shortread.txt" is not in the list of files to be read
6.Allow program time to run...
7. Once finished look for the generated sequence in "ANSWERS.txt"
9. Compare sequence in "ANSWERS.txt" to the sequence in "OrigionalStrand.txt"
