import base64, pickle, os, sys
from winreg import *
import tkinter as tk
from tkinter.filedialog import askopenfilenames

HEADERSIZE = 10

def recv_msg():
    while True:
        recv_msg = c.recv(1024)
        if not recv_msg:
            sys.exit(0)
        recv_msg = recv_msg.decode()
        return(recv_msg)

def send_msg(msg):
    while True:
        string = input(str(msg))
        data = string.encode()
        c.send(data)

def browse():
    root = tk.Tk()
    root.withdraw()
    file = askopenfilenames()
    return(file)

def name(file):
    filepath, filename = os.path.split(file)
    return(filename)

def enc(file):
    with open(file, "rb") as f:
        bytes = f.read()
        string = base64.b64encode(bytes)
        msg = pickle.dumps(string)
        return(msg)

def dec(data):
    string = pickle.loads(b"".join(data))
    file = base64.b64decode(string)
    return(file)

def appen(packet):
    data = []
    data.append(packet)
    return(data)

def savefile(filename, file):
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
        filepath = os.path.join(Downloads, filename)
    with open(filepath, 'wb') as f:
        f.write(file)

def recvall(sock):
    data = b''
    while True:
        packet = s.recv(4096)
        data += packet
        if len(packet) < 4096:
            break
        return data
