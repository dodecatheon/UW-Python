#!/usr/bin/env python
import time
import datetime

def date_time():
    return datetime.datetime.now()

if __name__ == "__main__":
    print "Here is the time: %s" % time.time()
    print "and again: %s" % datetime.datetime.now()
