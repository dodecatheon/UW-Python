#!/usr/bin/env python
"""
 Exercise 5B - Write a function sorted_list that takes one list
  argument and returns a list with the same elements but sorted.  This
  function must NOT change the list in the caller.  You may use the
  list sort method, but you may NOT use the built-in library function
  'sorted' in your solution.  Write your function in a module also
  named sorted_list that defines at least two test strings.  In your
  module, call your function on each of these lists and print the
  results.  Also, print both lists after calling the function to show
  that they have not changed.
"""
s = list('this is test string number one')
t = list('zyxwvutsr is the first part of the reversed alphabet')

def sorted_list(s):
    "sorted_list(s), where s is a list"

    temp = s[:]
    temp.sort()
    return temp

def test_sorted_list(s=s, t=t):
    print sorted_list(s)
    print sorted_list(t)
    print ''.join(s)
    print ''.join(t)
    

if __name__ == "__main__":
    # commandline execution, for debugging
    # Assume that two arguments are strings, convert them to lists:
    import sys
    if len(sys.argv) == 3:
        test_sorted_list(s=list(sys.argv[1]), t=list(sys.argv[2]))
    else:
        test_sorted_list()
else:
    # imported execution as per spec:
    test_sorted_list()
