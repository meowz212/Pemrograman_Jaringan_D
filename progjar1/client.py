import sys
import socket


serv_port = [5000, 5002]


for i in range(2):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.164.128', serv_port[i])
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
        print(f"sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        # Extra 12 expected amounts for IAC Commands
        while amount_received < (amount_expected + 6):
            data = sock.recv(16)
            amount_received += len(data)
            print(f"{data}")

    finally:
        print("closing")
        sock.close()
