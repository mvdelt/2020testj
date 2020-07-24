import socket

print(socket.gethostname())
print(socket.getfqdn())
print(socket.getfqdn(socket.gethostname()))
print(socket.gethostbyname((socket.gethostname())))