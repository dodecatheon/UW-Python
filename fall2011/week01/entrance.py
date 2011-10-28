#!/usr/bin/env python
def main(x):
    print "input x = ", x
    avg = sum(x) / float(len(x))
    print "decimal average = %.4g" % avg

if __name__ == "__main__":
    main([1,2,3,4,5,5.5,6,7,7,6])

