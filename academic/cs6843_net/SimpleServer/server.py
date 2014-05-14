# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
HOST = ''
PORT = 6789
serverSocket.bind((HOST, PORT))
serverSocket.listen(0)
while True:
    # Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        try:
            filename = message.split()[1]
        except IndexError:
            continue
        with open(filename[1:], 'r') as f:
            outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n')
        connectionSocket.send("Content-Type: text/html\r\n\r\n")
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n')
        connectionSocket.send("Content-Type: text/html\r\n\r\n")
        with open('404.html', 'r') as f:
            connectionSocket.send(f.read())
        # Send response message for file not found
        # Close client socket
        connectionSocket.close()

serverSocket.close()
