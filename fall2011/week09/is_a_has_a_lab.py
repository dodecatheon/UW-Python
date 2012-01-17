#!/usr/bin/env python
class D(dict):
    'An instance of D is a dictionary'
    # inherit __init__ from dict

    def __repr__(self):
        'prints as D({...}) vs. {...}'
        return 'D(%s)' % dict.__repr__(self)

class X(object):
    'An instance of X /has a/ dictionary'
    def __init__(self, d):
        assert isinstance(d, dict) # d must be dict
        self.d = d
        return None

    def __repr__(self):
        'prints as X({...}) vs. {...}'
        return 'X(%s)' % dict.__repr__(self.d)
    
d0 = {'a':1, 'b':2}

d, x = D(d0), X(d0)

print type(d), d, isinstance(d, D), isinstance(d, dict)
print type(x), x, isinstance(x, X), isinstance(x, dict)
print type(x.d), x.d, isinstance(x.d, X), isinstance(x.d, dict)

print d['a']
try:
    print x['a']
except:
    print "error with x['a']"
print x.d['a']
for c in d: print c

try:
    for c in x: print c
except:
    print "error for c in x: print c"

for c in x.d: print c

print dir(d)
print dir(x)

print set(dir(d)) - set(dir(x))
print set(dir(x)) - set(dir(d))


