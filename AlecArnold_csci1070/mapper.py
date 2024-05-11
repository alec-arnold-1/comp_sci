#!/usr/bin/env python
import sys

def mapper():
    """
    Reads in a sentence and maps the values
    """
    #stdin = standard input
    for line in sys.stdin:

        #strip white space at the beginning
        #and end of line
        line = line.strip()

        #split the line into words
        words = line.split()

        #process each word and assign
        #a value of 1 to each word
        for word in words:
            print(word+"\t1")

if __name__=="__main__":
    mapper()