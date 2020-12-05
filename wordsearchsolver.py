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
        
        print() # To make the output slightly prettier 
        # solves the word search, formats and prints the solutions (it would not hurt to further divide formatting/printing into separate functions)
        solve_wordsearch(dimensions, word_search, words_list)
        print() # For beauty, again. Hahah!
        
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

# I think there is a more elegant way to solve this, using recursion/dynamic programming or something similar,
# but due to time-constraints I cannot implement such a solution.
def solve_wordsearch(dimensions, word_search, words_list):
    for word in words_list:
        found = False
        count = 0
        # master while loop that exits when each word is found
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                start = [i, j]
                end = None # end will turn into list containing end-coordinates of matching word, if found.
                # if value in grid matches first letter in word 
                if word_search[i][j] == word[0]:
                    # These booleans start true and are flipped to False if the next while loop finds boundary errors in its
                    # search for a matching word
                    right_possible = True
                    down_possible = True
                    left_possible = True
                    up_possible = True
                    
                    # Each of these conditionals checks if word length is in bounds in the respective direction,
                    # checks for a match, and either breaks or continues
                    if (len(word) + j) <= (dimensions[0]):
                        end = check_right(i, j, dimensions, word_search, word)
                        # If end is changed from none, this if-statement ensures to break out of for loop if word is found
                        if end != None:
                            # Not a fan of these break statements, but they do the job for now
                            break 
                    else:    
                        right_possible = False                    


                    # Check down
                    if (len(word) + i) <= (dimensions[0]):
                        end = check_down(i, j, dimensions, word_search, word)
                        if end != None:
                            break
                    else:
                        down_possible = False

                    # Check left
                    if len(word) <= j:
                        end = check_left(i, j, dimensions, word_search, word)
                        if end != None:
                            break
                    else:
                        left_possible = False

                    # Check up
                    if len(word) <= i:
                        end = check_up(i, j, dimensions, word_search, word)
                        if end != None:
                            break
                    else:
                        up_possible = False
                    
                    # Only checks diagonals if they haven't been ruled out by the previous bounds checks
                    # Check down-right diagonal
                    if right_possible and down_possible:
                        end = check_dr_diag(i, j, dimensions, word_search, word)
                        if end != None:
                            break

                    # Check down-left diagonal
                    if down_possible and left_possible:
                        end = check_dl_diag(i, j, dimensions, word_search, word)
                        if end != None:
                            break

                    # Check up-left diagonal
                    if left_possible and up_possible:
                        end = check_ul_diag(i, j, dimensions, word_search, word)
                        if end != None:
                            break

                    # Check up-right diagonal
                    if up_possible and right_possible:
                        end = check_ur_diag(i, j, dimensions, word_search, word)
                        if end != None:
                            break

                    # if nothing is found yet, move on to next index in graph
            if end != None:
                # Breaks the outer loop and moves to next word, if end is found
                break
        # FINAL OUTPUT - the following line formats and prints the desired output.
        # the location of this output could be reworked, but it does the job!
        print(word, str(start[0])+":"+str(start[1]), str(end[0])+":"+str(end[1]))


# Each of the following 8 functions are called in solve_wordsearch(), and their purpose is to 
# check if a valid match is found in the wordsearch, in the respective direction for each function
# For example, the following function - check_right() - checks for further matches to the right of 
# an index that is found to match the first letter of a desired word
def check_right(i, j, dimensions, word_search, word):                    
    # Check to the right until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''
    for k in range(len(word)):
        potential_word += word_search[i][j+k]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i, j+k]
            return end
    # If no match, returns found = False and end = None
    return None

def check_down(i, j, dimensions, word_search, word):                    
    # Check down until word is found or invalidated
    # start new comparison string potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i+k][j]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i+k, j]
            return end
    # If no match, returns found = False and end = None
    return None


def check_left(i, j, dimensions, word_search, word):
    # Check to the left until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i][j-k]
        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i, j-k]
            return end
    # If no match, returns found = False and end = None
    return None

def check_up(i, j, dimensions, word_search, word):
    # Check upward until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i-k][j]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i-k, j]
            return end
    # If no match, returns found = False and end = None
    return None


def check_dr_diag(i, j, dimensions, word_search, word):
    # Check down-right diagonal until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i+k][j+k]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i+k, j+k]
            return end
    # If no match, returns found = False and end = None
    return None

def check_dl_diag(i, j, dimensions, word_search, word):
    # Check down-left diagonal until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i+k][j-k]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i-k, j+k]
            return end
    # If no match, returns found = False and end = None
    return None

def check_ul_diag(i, j, dimensions, word_search, word):
    # Check up-left diagonal until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i-k][j-k]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i-k, j-k]
            return end
    # If no match, returns found = False and end = None
    return None

def check_ur_diag(i, j, dimensions, word_search, word):
    # Check up-right diagonal until word is found or invalidated
    # start new comparison string AKA potential_word
    potential_word = ''

    for k in range(len(word)):
        potential_word += word_search[i-k][j+k]

        # if full match found, break out of loop with start + end points 
        if potential_word == word:
            end = [i-k, j+k]
            return end
    # If no match, returns found = False and end = None
    return None

if __name__ == "__main__":
    main()
    pass