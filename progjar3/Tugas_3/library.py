import logging
import os
import time
import datetime
import base64
import socket


def get_destination():
    dest = dict()
    dest['ip1'] = '192.168.122.110'
    dest['ip2'] = '192.168.122.120'
    return dest

def send_image(IP_ADDRESS):
    sckclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send Data
    namafile = "tes.jpg"
    ukuran = os.stat(namafile).st_size

    fp = open(namafile, 'rb')
    k = fp.read()
    terkirim = 0
    for x in k:
        k_bytes = bytes([x])
        sckclient.sendto(k_bytes, (IP_ADDRESS, 8888))
        terkirim = terkirim + 1
        print(k_bytes,f"terkirim {terkirim} of {ukuran} ")