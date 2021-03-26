import sys
import socket
import string
import random
import os.path

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servers = ["192.168.122.156", "192.168.122.105"]

# Connect the socket to the port where the server is listening
for i in range(2):
    server_address = (servers[i], 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

try:
    image = 'tes.png'
    message = os.path.getsize(image)
    name = input("Please input your expected filename:")

    # Send data
    print(f"sending {message} Bytes of Data")
    f = open(image, 'rb')
    l  = f.read(message)
    sock.sendall(l)
    f.close()

    # Look for the response
    amount_received = 0
    f2 = open(name + "_" + str(i) + ".png", 'wb')
    amount_expected = os.path.getsize(image)
    while amount_received < amount_expected:

        data = sock.recv(16)
        f2.write(data)
        amount_received += len(data)

    # print(f"{amount_received}")
    f2.close()

finally:
    print("closing")
    sock.close()