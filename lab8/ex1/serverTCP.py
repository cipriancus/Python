import socket
from time import gmtime, strftime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen(2)
f = open('tcpFile', 'w')

while True:
	(connection, address) = s.accept()
	x = ("Connectd address:",address, strftime("%Y-%m-%d %H:%M:%S", gmtime()));
	f.write(str(x))
	f.write('\n')
	while True:
		data = connection.recv(100).decode("UTF-8")
		if not data: break
		print("Received: ",data)
		if "exit" in data: break

connection.close()
print ("Server closed")