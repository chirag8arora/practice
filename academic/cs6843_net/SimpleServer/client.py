# import socket module
import sys
from socket import *
from datetime import datetime


def main(*args):
    # print args
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    HOST = args[1]
    PORT = int(args[2])
    serverSocket.connect((HOST, PORT))
    _get = "GET /%s\r\n" % args[3]
    _get += 'Accept:text/html\r\n'
    serverSocket.sendall(_get)
    # serverSocket.sendall('Accept:text/html')
    data = serverSocket.recv(1024)
    print data
    serverSocket.close()

if __name__ == '__main__':
    main(*sys.argv)
