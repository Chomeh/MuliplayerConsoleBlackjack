#Connect to a socket and send a single string

import socket 
while True:
	BUFFER_SIZE = 1024
	S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	S.connect(('127.0.0.1', 8089))
	data = S.recv(BUFFER_SIZE)
	print('received data:', data)
	if data.startswith(b'q'):
		reply = input('response: ').lower()	
		S.send(bytes(reply, 'UTF-8'))
	if data.startswith(b'n'):
		reply = input('Numerical response: ').lower()	
		S.send(bytes(reply, 'UTF-8'))

		#LEFT TO DO: 