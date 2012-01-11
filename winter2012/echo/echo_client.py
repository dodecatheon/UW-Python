"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50000 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port))
print "Enter string to send ==> ",
send_string = raw_input()
s.send(send_string) 
data = s.recv(size) 
s.close()
print 'from (%s,%s) %s' % (host, port, data)
receive_string = data.split(': ')[1]
print 'send_string matches receive_string?', send_string == receive_string

