#!/usr/bin/env python

import socket
import threading
import SocketServer
from time import sleep
import sys

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current == self.high:
            self.current = 0
            return self.high
        else:
            self.current += 1
            return self.current - 1
        
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    global ifc
    global counter

    def handle(self):
	while 1:

	        data = self.request.recv(1024)
		if not data:
			break
#        cur_thread = threading.current_thread()
        	response = '200 %s\n' % ifc[counter.next()] 
        	self.request.sendall(response)
		with open('/tmp/threaded.txt', 'a') as f:
                	f.write(data + '\n')
	return

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

#class MyTCPHandler(SocketServer.BaseRequestHandler):
  #counter = Counter(0, 3)
  
 # def handle(self):
    #self.request.settimeout(1)
 #   global ifc
  #  global counter
     
   # while 1:
    #	self.data = self.request.recv(1024).strip()
        #c = counter.next()
	
#	with open('/tmp/args.txt', 'a') as f:
#	        f.write(self.data + '\n')
#
#	if not self.data:
#		self.request.close()
#		break
#	data = '200 %s\n' % ifc[counter.current]
 #   	self.request.send(data)
#	counter.next()
 #   return

if __name__ == "__main__":
    ifc = []
    counter = None
    n = 4
    for i in xrange(n):
        ifc.append('interface-%d' % (i + 1))

    counter = Counter(0,len(ifc) - 1)
    

    HOST, PORT = "localhost", 12313

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    #Server_thread.daemon = True
    server_thread.start()
