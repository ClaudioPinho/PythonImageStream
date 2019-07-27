import socket
import png
import binascii
from PIL import Image
import PIL
import io

#Create a test image
#f = open('test.png', 'wb')
#w = png.Writer(255, 1, greyscale=True)
#f.close()

TCP_IP = 'localhost'
TCP_PORT = 1234
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
#Open the image file
f = open("image.png", "wb")
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	f.write(data)

print("Data Received!")
f.close()
conn.close()
