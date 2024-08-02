# client.py
import cv2
import socket
import struct
import pickle

# Connect to the remote server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((' https://hari417.github.io/drone/', 8485))  # Replace 'your_server_ip' with the actual server IP
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    data = pickle.dumps(frame)
    client_socket.sendall(struct.pack("L", len(data)) + data)

cam.release()
client_socket.close()
