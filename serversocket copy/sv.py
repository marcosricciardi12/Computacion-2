import socketserver
import multiprocessing
import signal, os
import argparse
import subprocess as sp
import pickle
import sys
import concurrent.futures

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        while True:
            self.data = self.request.recv(4096).strip()
            print(sys.getsizeof(self.data))
            self.data = pickle.loads(self.data)
            self.process = sp.Popen(self.data, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
            self.stdout, self.stderr = self.process.communicate()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            print(self.stdout)
            if self.stderr == b'':
                self.output = b'\nOK\n' + self.stdout
                self.output = pickle.dumps(self.output)
                self.request.sendall(self.output)
            else:
                self.output = b'\nERROR\n' + self.stderr
                self.output = pickle.dumps(self.output)
                self.request.sendall(self.output)
            print("PID: %d" % os.getpid())

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hola")
    parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto")
    parser.add_argument("-c", "--concurrency", type=str, required=True, help="Concurrencia: forking o threading")
    args = parser.parse_args()
    HOST, PORT = "", args.port
    socketserver.TCPServer.allow_reuse_address = True
    if args.concurrency == 'p':
        with ForkedTCPServer((HOST, PORT), MyTCPHandler) as server:

            server.serve_forever()
            server.shutdown()

    if args.concurrency == 't':
        with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()