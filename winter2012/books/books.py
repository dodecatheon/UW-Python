#!/usr/bin/env python
"""
Converting minimal Flask + forms demo into books website assignment.
- Write a multi page website, using bookdb.py
- Index page is a list of books, link to a detail page per book
- Each detail page displays info about one book
"""

from flask import Flask, render_template, request
import bookdb

# form_page is now a template

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

# View functions generate HTTP responses including HTML pages and headers

# Let's make the top level directory return the index
@app.route('/')
@app.route('/books.html')               # And handle books.html also
def index():
    return render_template('index.html', titles=titles)

@app.route('/book_details.py')
def book_details_page():
    book_id = request.args['id']
    book_info = books.title_info(book_id)
    return render_template('details.html', book_info=book_info)

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    books = bookdb.BookDB()            # Persistence of books
    titles = books.titles()           # Persistence of titles
    # For localhost only:  app.run()
    # For all hosts
    app.run(host='0.0.0.0')
