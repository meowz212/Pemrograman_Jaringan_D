import sys
import socket
import string
import random
import os.path
import base64

serv_port = [5000, 5002]


for i in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.164.128', 5000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        image = 'tes.png'
        message = os.path.getsize(image)
        name = input("Please input your expected filename:")

        # Send data
        print(f"sending {message} Bytes of Data")
        with open(image, 'rb') as f:
            l  = base64.b64encode(f.read())
            sock.sendall(l)
            f.close()

        # Look for the response
        amount_received = 0
        f2 = open(name + "_" + str(i) + ".png", 'wb')
        amount_expected = len(l)
        while amount_received < amount_expected:

            data = sock.recv(16)
            encode = base64.b64decode(data)
            f2.write(encode)
            amount_received += len(data)

        # print(f"{amount_received}")
        f2.close()

    finally:
        print("closing")
        sock.close()