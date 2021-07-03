import socket

UDP_IP_ADDRESS = '0.0.0.0'
UDP_PORT = 5050

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))

filename = 'encrypted.png'
fp = open(filename,'wb+')

while True:
    data, addr = serverSock.recvfrom(1024)
    count=count+len(data)
    print(addr," blok ", count,"panjang : ",len(data), data)
    fp.write(data)

with open('encrypted.png', 'rb') as f:
    l = base64.b64decode(f.read())

# Decode the encrypted Base64 Image
with open("decryptedimage" + ".png", 'wb') as f2:
    f2.write(l)
    f2.close()

f.close()