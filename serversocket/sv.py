import socketserver
import multiprocessing
import signal, os
import argparse
import subprocess as sp
import pickle
import sys
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print(sys.getsizeof(self.data))
        self.data = pickle.loads(self.data)
        self.process = sp.Popen(self.data, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
        self.stdout, self.stderr = self.process.communicate()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        print(self.stdout)
        # just send back the same data, but upper-cased
        if self.stderr == b'':
            self.output = b'\nOK\n' + self.stdout
            self.output = pickle.dumps(self.output)
            self.request.sendall(self.output)
        else:
            self.output = b'\nERROR\n' + self.stderr
            self.output = pickle.dumps(self.output)
            self.request.sendall(self.output)
        print("PID: %d" % os.getpid())
        signal.pause()

class ForkedTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sdasdas")
    parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto")
    parser.add_argument("-c", "--concurrency", type=str, required=True, help="Concurrencia: forking o threading")
    args = parser.parse_args()
    HOST, PORT = "", args.port
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 9999
    if args.concurrency == 'p':
        with ForkedTCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C

            # 
            #server_fork = multiprocessing.Process(target=server.serve_forever)

            #server_fork.daemon = True
            #server_fork.start()
            #server.shutdown()
    #        server.handle_request()
            server.serve_forever()
            server.shutdown()
    if args.concurrency == 't':
        with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C

    #        server_thread = threading.Thread(target=server.serve_forever)

    #        server_thread.daemon = True
    #        server_thread.start()

            server.serve_forever()

            # to wait connections
            try:
                signal.pause()
            except:
                server.shutdown()