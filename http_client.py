# Name: Carl Baptiste, StudentID: N01685318

from socket import *

# Initiating
server_name = "gaia.cs.umass.edu"
server_port = 80


# create tcp socket
client_socket = socket(AF_INET, SOCK_STREAM)

# connect to server
client_socket.connect((server_name, server_port))

# http request

request = (
    "GET /kurose_ross/interactive/index.php HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n"
)


# sending the http request
client_socket.send(request.encode())

# receive
response = client_socket.recv(4096)


print(response.decode())

client_socket.close()
