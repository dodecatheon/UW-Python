#!/usr/bin/env python
"""
decorator that turns a function into a generator
"""

def generator(f):
    def gen(s):
        for x in s:
            yield f(x)
        raise StopIteration
    return gen
    # Alternatively, can return a generator expression
    # def gen(s):
    #    return (f(x) for x in s)


@generator
def odd(x):
    return x % 2

for o in odd(range(4)): print o

print

@generator
def my_bool(x):
    return bool(x)

for b in my_bool([0,1,'','x',[],[0]]): print b

print

# can also apply the decorator function to an already-defined function

bg = generator(bool)  # Python's built-in bool function

for b in bg([0,1,'','x',[],[0]]): print b
