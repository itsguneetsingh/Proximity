import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))


data = b''

packet = s.recv(409600000)
data += packet
list = pickle.loads(data[HEADERSIZE])
print(list[0])
