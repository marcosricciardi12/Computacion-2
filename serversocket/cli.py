import socket
import argparse
import sys
import pickle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sdasdas")
    parser.add_argument("-j", "--host", type=str, required=True, help="Ingrese la direccion ip del host")
    parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto del host")
    args = parser.parse_args()
    HOST, PORT = args.host, args.port

    while True:
        data = input("> ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            print(data)
            data = pickle.dumps(data.encode())
            sock.sendall(bytes(data))

            msg_rcv = sock.recv(1024)
            sizz = sys.getsizeof(msg_rcv)
            print(sizz)
            received = pickle.loads(msg_rcv).decode()
            sizz = sys.getsizeof(received)
            print(sizz)
        print(received)
        