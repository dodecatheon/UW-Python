"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50001
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50001 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

prompt = "Enter string to send (hit RET to exit) ==> "
print prompt,
send_string = raw_input()

while send_string:
    s = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM) 
    s.connect((host,port))
    s.send(send_string) 
    data = s.recv(size) 
    s.close()
    print 'from (%s,%s) %s' % (host, port, data)
    receive_string = data.split(': ')[1]
    print 'send_string matches receive_string?', send_string == receive_string

    print prompt,
    send_string = raw_input()
