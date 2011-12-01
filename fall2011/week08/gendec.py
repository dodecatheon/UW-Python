#!/usr/bin/env python
"""\
Due Week09, 2011/12/05:
Create a decorator that turns a function into a generator
"""
def generator(f):
    def gendec(t):
        for x in t:
            yield f(x)
    return gendec

if __name__ == "__main__":
    @generator
    def odd(i):
        return i % 2
    
    for y in odd(xrange(1,4)): print y
    
"""
Results of run:
------------------------------------------------------------------------
ted@baobob:0 22:33:02 ~/uwpython/fall2011/week08
$ ./gendec.py 
1
0
1
ted@baobob:0 22:33:06 ~/uwpython/fall2011/week08
"""
