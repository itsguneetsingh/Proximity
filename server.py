import socket, pickle, sys
from modules import browse, name, enc


HEADERSIZE = 10

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    # After the Connection is established, open the browse menue
    files = browse()
    n = 0
    messagelist = []
    filenamelist = []
    filedatalist = []

    for filenames in files:
        file = files[n]
        filename = name(file)
        filedata = enc(file)
        n += 1

        # Save the filename and file location in a list
        filenamelist.append(filename)
        filedatalist.append(filedata)

    # Pickle the list and then send it in utf-8 format
    messagelist.append(filenamelist)
    messagelist.append(filedatalist)
    msg = pickle.dumps(messagelist)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    clientsocket.send(msg)


    # Close client and then the program as well
    clientsocket.close()
    sys.exit()
