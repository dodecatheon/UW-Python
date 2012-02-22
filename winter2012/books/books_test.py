#!/usr/bin/env python
"""
Demonstrate Flask test support: test without server
"""

import books as e

# Flask test support
tc = e.app.test_client()
print tc
print
print

# should respond with 404
r = tc.get('/')
print r
print r.data
print
print

# should respond with form
r = tc.get('/books.html')
print r
print r.data
print
print

# should respond with message page
r = tc.get('/books.py?message=Hello')
print r
print r.headers
print r.data
print
print

# This will fail if application isn't working
assert 'Hello' in r.data  # demonstrate success
assert 'Goodbye' in r.data # demonstrate failure
