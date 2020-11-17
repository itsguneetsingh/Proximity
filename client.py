import socket, pickle, sys
from modules import savefile

HEADERSIZE = 10

# Create a socket and then connect to the ip
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))
print("Connected to the server")


print("Ready to recieve messages")

data = b''
new_msg = True
while True:
    packet = s.recv(409600000)

    if not packet:
        break

    data += packet


list = pickle.loads(data[HEADERSIZE:])
filenamelist = list[0]
filedatalist = list[1]

for n in range(len(filenamelist)):
    filename = filenamelist[n]
    filedata = filedatalist[n]

    savefile(filename, filedata)
    print("file saved")

s.close()
sys.exit()
