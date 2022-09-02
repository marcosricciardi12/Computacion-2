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

    # Create a socket (SOCK_STREAM means a TCP socket)
    while True:
        data = input("> ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            print(data)
            data = pickle.dumps(data.encode())
            sock.sendall(bytes(data))

            # Receive data from the server and shut down
            msg_rcv = sock.recv(1024)
            sizz = sys.getsizeof(msg_rcv)
            received = pickle.loads(msg_rcv).decode()
        print(received)
        print(sizz)