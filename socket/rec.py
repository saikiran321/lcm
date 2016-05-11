import socket

HOST = '192.168.1.124'                 # Symbolic name meaning all available interfaces
PORT = 50006             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# print 'Connected by', addr
while 1:
	s.listen(1)
	conn, addr = s.accept()
	data = conn.recv(1024)
	if data:
		print "msg recieved"
		print data	

conn.close()