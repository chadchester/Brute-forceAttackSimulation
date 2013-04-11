import socket

serverSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
serverSocket.bind( ('',12345) );
serverSocket.listen(5)

while 1:
	clientSocket, (remoteHost, remotePort) = serverSocket.accept()
	loginMessage = clientsocket.recv(100)
	username = loginMessage.split(' ')[0]
	password = loginMessage.split(' ')[1]
	if username =='Samuel' and password == '897375' :
		clientSocket.send('OK')
	else:
		clientSocket.send('FormatError or Auth failed')
