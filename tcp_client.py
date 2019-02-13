# TCP Client

import socket

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print response

"""Assumptions:-"""
# 1. Connection will always succeed.
# 2. Server is expecting us to send data first.
# 3. Server sends data back in a timely fashion.