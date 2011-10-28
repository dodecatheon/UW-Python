#!/usr/bin/env python
"""
Assignment due week 4, Tues Nov 1, bring exercise to turn in (hardcopy)

 Required reading: Ch. 10, 12, 13, 14

 Exercise: 12.3 in Downey - write the function most_frequent that takes a string
 and prints the letters in decreasing order of frequency. ...
"""
from string import ascii_uppercase, ascii_lowercase
from operator import itemgetter

def reverse_sort_dict(d):
    return sorted(d.iteritems(), key=itemgetter(1), reverse=True)

def most_frequent(s):
    # Here is a string that contains all letters
    all_letters = ascii_uppercase + ascii_lowercase

    # Initialize the count dictionary
    letter_count = {}
    for c in s:
        if c in all_letters:
            letter_count[c] = letter_count.get(c,0) + 1

    sorted_count = reverse_sort_dict(letter_count)
    for c, count in sorted_count:
        print "%s:\t%6d" % (c, count)

    return sorted_count

def main():
    import sys
    "Enter string as the first argument, or read from stdin"
    if len(sys.argv) != 2:
        s = sys.stdin.read()
    else:
        s = sys.argv[1]

    sc = most_frequent(s)
    return sc

if __name__ == "__main__":
    main()
