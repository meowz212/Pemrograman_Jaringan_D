import sys
import socket
import string
import random
import os.path
import base64

serv_port = [5000, 5002]

name = input("Please input your expected filename:")

for i in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.164.128', serv_port[i])
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        image = 'tes.png'
        message = os.path.getsize(image)


        # Send data
        print(f"sending {message} Bytes of Data")
        with open(image, 'rb') as f:
            l  = base64.b64encode(f.read())
            sock.sendall(l)
            f.close()

        # Look for the response
        amount_received = 0
        f2 = open('encrypted' + str(i) + '.png', 'wb')
        amount_expected = len(l)
        while amount_received < (amount_expected + 12):

            data = sock.recv(16)
            f2.write(data)
            amount_received += len(data)

        # print(f"{amount_received}")
        f2.close()

        #Open the encrypted file
        with open('encrypted' + str(i) + '.png', 'rb') as f:
            l = base64.b64decode(f.read())

        #Encode the encryted Base64 Image
        with open(name + "_" + str(i) + ".png", 'wb') as f2:
            f2.write(l)
            f2.close()

        f.close()

    finally:
        print("closing")
        os.remove('encrypted' + str(i) + '.png')
        sock.close()