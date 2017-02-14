from socket import *

HOST=' localhost '
PORT = 7890
BUFSIZ = 1024
ADDR = (HOST,PORT)

while True
    tcpClisock = socket(AF_INET,SOCK_STREAM)
    tcpClisock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpClisock.send('%s\r\n' % data)
    data = tcpClisock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpClisock.close()
