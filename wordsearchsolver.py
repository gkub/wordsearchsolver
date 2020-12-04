# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# wordsearchsolver.py                                                         #
# --------------------------------------------------------------------------- #
# Word Search Solver                                                          #
# Written by Gregory Kubiski                                                  #
# Dec 03, 2020                                                                #
# Written and tested in Python 3.7.4 - Requires at least Python 3.7 or newer  #
# No packages beyond the standard library are installed or used               #
# --------------------------------------------------------------------------- #
# This program is a word search solver.                                       #
# It takes an input text file of the following format:                        #
#                                                                             #
# 5x5                                                                         #
# H A S D F                                                                   #
# G E Y B H                                                                   #
# J K L Z X                                                                   #
# C V B L N                                                                   #
# G O O D O                                                                   #
# HELLO                                                                       #
# GOOD                                                                        #
# BYE                                                                         #
#                                                                             #
# (The first line is '5x5' and the last line is 'BYE")                        #
#                                                                             #
# The program then searches the given NxN (in this case 5x5) matrix for the   #
# words provided at the end of the file, and outputs their location in the    #
# grid in the following format:                                               #
#                                                                             #
# HELLO 0:0 4:4                                                               #
# GOOD 4:0 4:3                                                                #
# BYE 1:3 1:1                                                                 #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# sys and pathlib imported for following line of code that version-checks Python
import sys
from pathlib import Path 
import pdb

# The following two lines of code ensure that the user is running the correct version of Python (or newer)
MIN_PYTHON_VERSION = (3, 7)
assert   sys.version_info >= MIN_PYTHON_VERSION, f"requires Python {'.'.join([str(n) for n in MIN_PYTHON_VERSION])} or newer"

# main function
def main():

    # Receives the file name from the user/stdin
    file_name = input("\nEnter the name of the text file containing your input word search:\n")
    
    # Checks if file name is a file in the same directory as this program or not
    filename_bool = Path(file_name).is_file() 
    
    # If not a file, tell the user and prompt them to exit
    if filename_bool == False:
        input("\nInvalid entry. Please ensure that your file is located IN THE SAME DIRECTORY as this program, and that your spelling is correct.\nPress Enter to exit the program\n")
    
    # Else if the file exists, continue program
    else:
        # Processes the file and returns the required information to find the given word search's solutions as a 3-component tuple
        dimensions, word_search, words_list = process_file(file_name)
        
        # solves the word search and returns the solutions
        solutions = solve_wordsearch(dimensions, word_search, words_list)
        
# intakes file, parses it for critical data, and returns the data in the form of a tuple:
# (dimensions, wordsearch, wordslist)
def process_file(file_name):
    with open(file_name, "r") as in_file:
            
        # Read the first line of the input file to get the dimensions of the word search
        dimensions_str = in_file.readline()

        # Convert the retrieved dimensions from strings to integers 
        dimension_x = int(dimensions_str[0]) # x-dimension, AKA number of columns
        dimension_y = int(dimensions_str[2]) # y-dimension, AKA number of rows

        # pack dimensions for return to the main function
        dimensions = [dimension_x, dimension_y]

        word_search = [] # an empty list, to be filled with the data from the input word search
            
        # These for-loops populate wordsearch with the proper characters from the input file 
        for i in range(dimension_y):
            input_row = in_file.readline()
            word_search.append([])
            for j in range(dimension_x):
                word_search[i].append(input_row[2*j])
            
        words_list = [] # an empty list, to contain all of the words in the word search
            
        # This for-loop finishes reading the input file, populates our list of words, and strips them of the \n at the end of each line
        for line in in_file:
            words_list.append(line.strip())
        # Return all the extracted data
        
    return(dimensions, word_search, words_list)

# There is certainly a more elegant way to solve this, using recursion/dynamic programming or something similar,
# but due to time-constraints I cannot implement such a solution.
def solve_wordsearch(dimensions, word_search, words_list):
    for word in words_list:
        #print(word)
        found = False
        count = 0
        # master while loop that exits when each word is found
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                print(word_search[i][j])
                # if value in grid matches first letter in word 
                if word_search[i][j] == word[0]:
                    right_possible = True
                    left_possible = True
                    up_possible = True
                    down_possible = True

                    
                    # Check bounds to the right
                    # If out of bounds, skip this block
                    if (len(word)+ i) > (dimensions[0]):
                        right_possible = False
                    else:
                        # Check to the right until word is found or invalidated
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        # SET UP PROPERLY AFTER NAP
                        for k in range(len(word)):
                            index = word_search[i+k][j]
                            potential_word += index
                            #print(potential_word)
                            #pdb.set_trace()
                        # if full match found, break out of loop with start + end points 
                        if potential_word == word:
                            start = word_search[i][j]
                            end = word_search[i+k][j]
                            found = True
                            print('found')
                            break


                    # If no match, then check down
                    
                    # Check bounds downward
                    # If out of bounds, break loop
                    if (len(word) + j) > (dimensions[1]):
                        down_possible = False
                    else:
                        # Check down until word is found or invalidated
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)):
                            index = word_search[i][j+k]
                            if index == word[k]:
                                potential_word += index
                                # if full match found, break out of loop
                                if potential_word == word:
                                    start = word_search[i][j]
                                    end = word_search[i][j+k-1]
                                    found = True
                                    break

                                        

                    # If no match, then check left

                    # Check bounds to the left
                    # If out of bounds, break loop
                    if (len(word)-1) > (i):
                        left_possible = False
                    else:
                        # Check to the left until word is found or invalidated
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)-1):
                            index = word_search[i-k][j]
                            if index == word[k]:
                                potential_word += index
                                # if full match found, break out of loop
                                if potential_word == word:
                                    start = word_search[i][j]
                                    end = word_search[i-k][j]
                                    found = True
                                    break
                                else:
                                    break

                                
                    
                    # If no match, then check up

                    # Check bounds to the right
                    # If out of bounds, break loop
                    if (len(word)-1) > (j):
                        up_possible = False
                    else:
                        # Check to the right until word is found or invalidated
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)-1):
                            index = word_search[i][j-k]
                            if index == word[k]:
                                potential_word += index
                                if potential_word == word:
                                    start = word_search[i][j]
                                    end = word_search[k][j-k]
                                    found = True
                                    break
                                else:
                                    break
                                
                
                    # diagonals do not need to do bounds checks, because this was already done for their 2D components
                    # If no match, then check down-right diagonal
                    if (right_possible == True) and (down_possible == True) and (found == False):
                        # Check to the right until word is found or invalid
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)-1):
                                index = word_search[i+k][j+k]
                                if index == word[k]:
                                    potential_word += index
                                    if potential_word == word:
                                        start = word_search[i][j]
                                        end = word_search[i+k][j+k]
                                        found = True
                                    break
                                else:
                                    break
                                    
                    
                    # If no match, then check down-left diagonal
                    if (left_possible == True) and (down_possible == True) and (found == False):
                        # Check to the right until word is found or invalid
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)-1):
                                index = word_search[i-k][j+k]
                                if index == word[k]:
                                    potential_word += index
                                    if potential_word == word:
                                        start = word_search[i][j]
                                        end = word_search[i-k][j+k]
                                        found = True
                                        break
                                else:
                                    break
                    
                    # If no match, then check up-left diagonal
                    if (left_possible == True) and (down_possible == True) and (found == False):
                        # Check to the right until word is found or invalid
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)-1):
                                index = word_search[i-k][j-k]
                                if index == word[k]:
                                    potential_word += index
                                    if potential_word == word:
                                        start = word_search[i][j]
                                        end = word_search[i-k][j-k]
                                        found = True
                                        break
                                else:
                                    break
                    
                    # Finally, check up-right if no other matches yet
                    if (left_possible == True) and (down_possible == True) and (found == False):
                        # Check to the right until word is found or invalid
                        # start new comparison string AKA potential_word
                        potential_word = ''
                        for k in range(len(word)-1):
                                index = word_search[i+k][j-k]
                                if index == word[k]:
                                    potential_word += index
                                    if potential_word == word:
                                        start = word_search[i][j]
                                        end = word_search[i+k][j-k]
                                        found = True
                                        break
                                else:
                                    break
                            



                    

            


            
'''for line in input_file:
            print(line)
        input_file.close()
        pass'''


        
    




'''
from tkinter import *

root = Tk() #

# Creates label widget
myLabel = Label(root, text="Label")
# Packs label to GUI
myLabel.pack()

root.mainloop()
'''
if __name__ == "__main__":
    main()
    pass