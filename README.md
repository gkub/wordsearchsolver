README for wordsearchsolver.py

-----------------

This program was written and tested in Python 3.7.4, and should work on all versions of Python from 3.7 upward.
There are no dependencies/packages required outside of Python's standard library, so no package manager is required.

wordsearchsolver.py is a basic word search solver

The easiest way to use the program is to place a text file of the following format ***in the same directory as wordsearchsolver.py***:

5x5
H A S D F
G E Y B H
J K L Z X
C V B L N
G O O D O
HELLO
GOOD
BYE


-----------------

Simply run wordsearchsolver.py with Python 3.7 (or greater - versions beyond 3.7.4 are untested but should still work, as of Dec 04, 2014) installed on your computer,
and it will prompt you to enter the name of the file you want to open. 

For example, when the program prompts you to "Enter the name of the text file containing your input word search:", if your text file is named "test.txt", you simply must type "test.txt" (without quotation marks) and the program should run as intended.

***As long as the file is in the same folder/directory as wordsearchsolver.py*** (or you enter the correct path relative to the location of worsearchsolver.py), the program will proceed to solve the word search contained in the input text file, and output the solutions in the following format:

HELLO 0:0 4:4
GOOD 4:0 4:3
BYE 1:3 1:1

The output is given on the command line, as required by the program specifications.


This program was authored/developed by Gregory Kubiski