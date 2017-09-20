#!/usr/bin/python
#coding=utf8

from collections import Counter
import sys, getopt, string

# prints usage informations
def usage():
    print 'Usage: \n'
    print 'char_frequency_analyser.py -i <input_text_file> \n'
    print "example: char_frequency_analyser.py -i textToAnalyse.txt \n"
    
# fetches options and arguments from CLI
def fetchOptsAndArgs(argv):

    in_file = ''

    try:
        opts, args = getopt.getopt(argv,"hi:",["help", "in_file="])
      
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print("") 
            usage()
            sys.exit()
        elif opt in ("-i", "--in_file"):
            in_file = arg
    
    return [in_file]    
    
# returns a counter object from input file
def count_occurences(in_file):
    if in_file != None:
        return Counter(in_file)

# returns a list containing the number of appearance of all characters in file
def most_common(counter):
    if counter != None:
        return counter.most_common()

if __name__ == "__main__":

    # options and arguments fetching
    args = fetchOptsAndArgs(sys.argv[1:])
    
    # if first args is not empty
    if args[0]: 

        try:
            file = open(args[0],'r').read()

        except IOError as err:
            print("File does not exist : "+err.filename)
            sys.exit(2)

        print("")
        print("analysing file "+args[0]+" ... \n")

        counter = count_occurences(file)
        result = most_common(counter)

        # prints each character and its number of appearance
        for r in result:

            # if whitespace or line break, don't display the information
            if r[0] == ' ':
                 continue
            elif r[0] == '\n':
                 continue
            else:
                print (r[0]+" appears "+str(r[1])+ " times")    
    else:
        print("") 
        usage()
        sys.exit(2)