import sys
import socket
import string
import random


serv_port = [5000, 5002]


for i in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.164.128', serv_port[i])
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
        while amount_received < (amount_expected + 12) :
            data = sock.recv(16)
            amount_received += len(data)

    finally:
        print("closing")
        print("last 16 strings: " + message[-16:])
        sock.close()