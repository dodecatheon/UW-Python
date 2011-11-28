#!/usr/bin/env python
"""
Write a module bag.py that defines a class named bag.  A bag (also
called a multiset) is a collection without order (like a set) but with
repetition (unlike a set) --- an element can appear one or more times
in a bag.  Implement bag as a subclass of dictionary where each bag
element is a key and its value is an integer that represents its
multiplicity (the number of repetitions).  For example in b1 =
bag({'a':2, 'b':3}), b1 is a bag where 'a' occurs twice (has
multiplicity 2) and 'b' occurs three times.  Provide a bag union
operator + (plus sign) that operates on two bags and returns a third
bag, their union.  The bag union contains all of the elements of both
bags, with their multiplicities added.  For example, after b2 =
bag({'b':1, 'c':2}), then b1 + b2 == bag({'a':2, 'b':4', 'c':2})
"""

class bag(dict):
    def __repr__(self):
        return 'bag(%s)' % super(bag,self).__repr__()

    def __init__(self,data):
        try:                    # dict or bag input
            for k, v in data.iteritems():
                self[k] = self.get(k,0) + v
        except:                 # basic iterable input, such as list
            for k in data:
                self[k] = self.get(k,0) + 1
 
    def __add__(self,other):
        "This works for adding a list, dict or bag"
        b = bag(self)
        for k, v in bag(other).iteritems():
            b[k] = b.get(k,0) + v
        return b

if __name__ == '__main__':        
    b1 = bag({'a':2, 'b':3})
    b2 = bag({'b':1, 'c':2})
    print "Should be b1 + b2 == bag({'a':2, 'b':4', 'c':2})"
    print b1 + b2

    b3 = bag(['b', 'a', 'b', 'a', 'b'])
    b4 = bag(['c', 'b', 'c'])
    print "b3 = bag(['b', 'a', 'b', 'a', 'b']) =", b3
    print "b4 = bag(['c', 'b', 'c']) =", b4
    print "b3 + b4 =", b3 + b4
