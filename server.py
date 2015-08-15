##Basic Server Module

import socket
from liblo import *
import sys
from threading import *

HOST = ''
PORT = 8080

#Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding the socket
try:
	s.bind((HOST, PORT))
	print('Bind successful.')
except socket.error as error:
	print ("Failed to bind. Code " + error[0] + ": " + error[1])
	sys.exit()

#Socket now listens
s.listen(10)
print('Listening...')

while True:
	connection, address = s.accept()
	print('Connected to ' + address[0] + ':' + str(address[1]))

s.close()