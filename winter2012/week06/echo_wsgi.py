"""
Minimal WSGI + forms demo, with persistence

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_wsgi.html

Based on example in PEP 333, then add path and query processing
"""

import urlparse

# send one of these pages, depending on URL path

form_page = """<head>
<title>Echo request</title>
</head>
<body>
<form method="GET" action="echo_wsgi.py">
Message: <input type="text" name="message" size="40">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""

message_template = """
<html>
<head>
<title>Echo response</title>
</head>
<body>
%s
</form>
</body>
</html>
"""

notfound_template = """
<html>
<head>
<title>404 Not Found</title>
</head>
<body>
404 %s not found
</form>
</body>
</html>
"""

messages = []
unhandled_queries = []

# must be named 'application' to work with our wsgi simple server
def application(environ, start_response):
    global messages
    global unhandled_queries
    status = '200 OK'
    response_headers = [('Content_type', 'text/HTML')]
    start_response(status, response_headers)
    # send different page depending on URL path
    path = environ['PATH_INFO']
    if path == '/echo_wsgi.html':
        page = form_page
    elif path == '/echo_wsgi.py':

        # Generalize the query so that we can do a number of different options
        query_string = urlparse.parse_qs(environ['QUERY_STRING'])
        print query_string

        # Brian asked me to do some extra credit, to handle other
        # sorts of queries:
        if query_string.has_key('message'):
            # This is what you asked for in the assignment
            messages.append('Message %d: %s' % (
                len(messages)+1,
                query_string['message'][0]))
            page = message_template % '<br>\n'.join(messages)
        else:
            # This is a logging honeypot ... it shows what queries have
            # been tried, the entire time the server has been up.
            i = len(unhandled_queries)
            for query, arglist in query_string.iteritems():
                i +=1
                unhandled_queries.append(
                    'Query number %d, "%s", with argument "%s", not handled yet' % \
                    (i, query, arglist[0] ))
            page = message_template % '<br>\n'.join(unhandled_queries)

    else:
        page = notfound_template % path
    return [ page ] # list of strings - must return iterable, not just a string
