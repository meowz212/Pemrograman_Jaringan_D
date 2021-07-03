import logging
import os
import time
import datetime
import base64
import socket


def get_destination():
    dest = dict()
    dest['ip1'] = ''
    dest['ip2'] = ''
    dest['ip3'] = ''
    return dest


def send_image(IP_ADDRESS):
    sckclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (IP_ADDRESS, 5050)
    print(f"connecting to {server_address}")
    sckclient.connect(server_address)

    image = 'tes.png'
    message = os.path.getsize(image)

    # Send Data
    print(f"sending {message} Bytes of Data")
    with open(image, 'rb') as f:
        l = base64.b64encode(f.read())
        sckclient.sendall(l)
        f.close()
