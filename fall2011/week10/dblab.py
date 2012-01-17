#!/usr/bin/env python
"""\
Write a python program that achieves the same effect without using any
database libraries.  Use an in-memory database consisting only of
built-in data Python structures (sets and tuples), and queries
consisting only of ordinary Python expressions (list comprehensions).
"""
from pprint import pprint

sample_mailing_list = [('philg@mit.edu',
                        'Philip Greenspun'),
                       ('ogrady@fastbuck.com',
                        "Michael O'Grady")]

sample_phone_numbers = [('ogrady@fastbuck.com',
                         'work',
                         '(800) 555-1212'),
                        ('ogrady@fastbuck.com',
                         'home',
                         '(617) 495-6000'),
                        ('philg@mit.edu',
                         'work',
                         '(617) 253-8574')]

ml_database = set(sample_mailing_list)
pn_database = set(sample_phone_numbers)

pprint(ml_database)
print

pprint(pn_database)
print

pprint([(email1, name1, email2, loc, number)
        for email1, name1 in ml_database
        for email2, loc, number in pn_database
        if email1 == email2])

