import socket
import argparse
import sys
import pickle
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sdasdas")
    parser.add_argument("-j", "--host", type=str, required=True, help="Ingrese la direccion ip del host")
    parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto del host")
    args = parser.parse_args()
    HOST, PORT = args.host, args.port

    
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        while True:
            data = input("> ")
            print(data)
            data = pickle.dumps(data.encode())
            sock.sendall(bytes(data))
            msg = sock.recv(1024)
            aux_tam = sys.getsizeof(msg)
            while int(aux_tam)>=1024:
                aux = sock.recv(1024)
                aux_tam = sys.getsizeof(aux)
                msg = msg + aux
            received = pickle.loads(msg).decode()
            print(received)
        