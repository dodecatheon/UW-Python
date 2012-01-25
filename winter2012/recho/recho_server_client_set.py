"""
echo server, usage:

 python echo_server.py <port>

Port is optional, default: 50001
"""

import socket 
import sys
from OrderedSet import OrderedSet

host = '' 
port = 50001 

if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'recho_server listening on port', port
s.listen(backlog) 

clients = OrderedSet([])
while True: 
    client, address = s.accept()
    # Add new client
    clients.add(client)

    data = client.recv(size) 
    if data: 
	for c in clients:
	    c.send('dodecatheon: %s' % data) 
	    print 'from %s: %s' % (address, data)
    else:
        client.send('dodecatheon: %s' % data) 
        client.close()
