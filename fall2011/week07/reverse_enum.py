#!/usr/bin/env python

def reverse_enum(data):
    for index in xrange(len(data)-1, -1, -1):
        yield index, data[index]

s = [c for c in 'supercalifragilisticexpialidocious']
for i, c in reverse_enum(s):
    if c == 'i':
        print "deleting at location", i
        del s[i]

print ''.join(s)
