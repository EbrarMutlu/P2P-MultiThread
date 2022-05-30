import os
import socket
from tkinter import filedialog

from tqdm import tk

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
#host = "192.168.1.101"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
filename = "data.txt"
# get the file size
filesize = os.path.getsize(filename)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input("> ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            file = open("data.txt", "r")
            data = file.read()

            """ Sending the filename to the server. """
            client.send("data.txt".encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            """ Sending the file data to the server. """
            client.send(data.encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            """ Closing the file. """
            file.close()
    client.close()

if __name__ == "__main__":
    main()

