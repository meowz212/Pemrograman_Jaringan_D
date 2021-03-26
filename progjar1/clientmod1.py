import sys
import socket
import string
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

i = 2
servers = ["192.168.122.156", "192.168.122.105"]

# Connect the socket to the port where the server is listening
for i in range(2):
    server_address = (servers[i], 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

try:
    loopnum = 2097152
    # Send data
    message = ''.join(random.choice(string.ascii_lowercase) for x in range(loopnum))

    print(f"output size: ", len(message) / 1024, "kb")
    print(f"sending string")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"{data}")
finally:
    print("closing")
    sock.close()