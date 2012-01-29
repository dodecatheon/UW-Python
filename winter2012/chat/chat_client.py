"""
chat client, usage:

 python chat_client.py <host> <port>

Both host and port are optional, defaults: localhost 50003
host must be present if you want to provide port

Prompt user for each message to send
Repeat sending messages until user enters empty string
"""

import socket 
import sys
import select
from pprint import pprint

host = 'localhost' 
port = 50003 # different default port than echo, both can run on same server
size = 1024

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, 
                       socket.SOCK_STREAM) 
client.connect((host,port)) 
print 'Connection accepted by (%s,%s)\nYou> ' % (host, port),
inputs = [client, sys.stdin]
running = True
timeout = 10
while running:
    in_ready, out_ready, exc_ready = select.select(inputs,[],[],timeout)

    for s in in_ready:
        if s == client:
            # handle the client socket
            data = s.recv(size)
            if data:
                print data
            else:
                print "\nEmpty data, exiting ..."
                running = False
        elif s == sys.stdin:
            # handle stdin
            msg = sys.stdin.readline()
            if msg:
                client.send(msg)
                print 'You> ',
            else:
                print "\nmsg is empty, close and exit ..."
                running = False
        else:
            print "\nI don't know what this should be ..."
            running = False
 
client.close()
