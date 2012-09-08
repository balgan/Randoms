# Echo server program
import socket, select
import random
import string
import time
import array
import sys
import os

##this version waits for a connect and then closes that port and opens another one :D


def openrandom():
	while(True):
		HOST = ''                 #All interfaces
		PORT = random.randrange(1025,65636)              # Random port
		print 'Opened port: ' + str(PORT) 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((HOST, PORT))
		s.listen(1)
		conn, addr = s.accept()
		conn.close()

openrandom()
