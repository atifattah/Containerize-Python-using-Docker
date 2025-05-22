import time
import socket
from sklearn.datasets import load_iris

data = load_iris()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 9999))

server.listen()

print("Server is listening on port 9999...")

while True:
    print("Waiting for connections...")
    client, addr = server.accept()
    print("Connected from", addr)
    client.send("You are connected now!\n".encode())
    client.send(f"{data['data'][:,0]}\n".encode())
    time.sleep(2)
    client.send("You are being disconnected now.\n".encode())
    client.close()
