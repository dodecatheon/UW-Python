#!/usr/bin/env python
"""
Assignment due week 3, Tues Oct 25, bring exercise to turn in (hardcopy)

 Required: Ch. 8, 9, 14
 Optional: http://docs.python.org/library/stdtypes.html#string-methods
            http://docs.python.org/howto/regex.html
            http://docs.python.org/howto/unicode.html
	    http://farmdev.com/talks/unicode/

 Exercise: Write a function named concordance that takes three
  arguments: a string, a file object for a file that is open for
  reading, and a file object for a file that is open for writing.  The
  function writes in the output file the line numbers and contents of all the lines
  in the input file where the string occurs.  Write the function in a module
  concordance.py that also opens the input and output files, calls the function,
  and closes the files.
"""
import re
def concordance(s, in_file, out_file):
    "s = string, in_file = file opened for reading, out_file = file opened for writing"
    for i, line in enumerate(in_file):
        if re.search(s, line):
            print "Found string '%s' on line %d of file' " % (s, i)
            print >>out_file, "Line %10d:\t%s" % i, line.rstrip()
    return

def run_concordance(s, in_filename, out_filename):
    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'w')
    concordance(s, in_file, out_file)
    in_file.close()
    out_file.close()
    return

def main():
    "arg1 is the string, arg2 is the input filename, arg3 is the output filename"
    import sys
    if len(sys.argv) != 4:
        print >>sys.stderr, "Error! enter 3 arguments only:  string, input file and output file."  
    s, in_filename, out_filename = sys.argv[1:]
    run_concordance(s, in_filename, out_filename)
    return

if __name__ == "__main__": 
    main()
