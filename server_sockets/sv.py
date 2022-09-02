#!/usr/bin/python3
import socket, os, multiprocessing, sys, signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def mp_server(c):
    print("Launching proc...")
    sock,addr = c
    while True:
        msg = sock.recv(1024)
        print(len(msg.decode()[:-2]))
        print("Recibido: '%s' de %s" % (msg.decode(), addr))
        if msg.decode()[:-2] == "exit":
            print("\nLlego un exit")
            sock.close()
            os._exit(0)
        msg = msg.decode().upper()
        sock.send(msg.encode("ascii"))
        



# create a socket object
# crea un objeto tipo socket para usarlo en la comunicación
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get local machine name
#host = socket.gethostname()
host = ""
port = int(sys.argv[1])

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    cliente = serversocket.accept()

    clientsocket, addr = cliente

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    child = multiprocessing.Process(target=mp_server, args=(cliente,))
    child.start()