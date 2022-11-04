"""
By: Mahad Osman
Exercise: Python Syntax 
Date: Nov 4th, 2022
"""
def print_upper_words(words, must_start_with):
    """ A function that accepts a lists of words and returns them capitalized"""
    for word in words:
        for char in must_start_with:
            if(word[0] == char):
                #print(word[0])
                print (word.upper())
                break
            #else:
                
