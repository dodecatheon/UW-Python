#!/usr/bin/env python
"""\
Due Week09, 2011/12/05:
Create a decorator that turns a function into a generator
"""
from functools import wraps
def generator(f):
    @wraps(f)
    def gendec(t):
        for x in t:
            yield f(x)
        # raise StopIteration not necessary!  t itself raises StopIteration!
    return gendec

if __name__ == "__main__":
    @generator
    def odd(i):
        "Input i.  Returns 0 if i even, 1 if i odd."
        return i % 2
    
    for y in odd(xrange(1,4)): print y
    
    print ""
    print "odd.__name__ =", odd.__name__
    print "odd.__doc__ =", odd.__doc__
"""
ted@baobob:0 20:01:44 ~/uwpython/fall2011/week08
$ ./gendec.py
1
0
1

odd.__name__ = odd
odd.__doc__ = Input i.  Returns 0 if i even, 1 if i odd.
ted@baobob:0 20:01:46 ~/uwpython/fall2011/week08
$ 
"""
