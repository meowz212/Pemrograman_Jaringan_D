import socket

UDP_IP_ADDRESS = ''
UDP_PORT = 8888

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))

filename = 'tesfinished.jpg'
fp = open(filename,'wb+')
count = 0

while True:
    data, addr = serverSock.recvfrom(1024)
    count=count+len(data)
    print(addr," blok ", count,"panjang : ",len(data), data)
    fp.write(data)

fp.close()