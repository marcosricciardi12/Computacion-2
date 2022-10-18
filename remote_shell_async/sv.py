import socketserver
import multiprocessing
import signal, os
import argparse
import subprocess as sp
import pickle
import sys
import asyncio
import time


async def handle(reader, writer):
    while True:
        data = await reader.read(4096)
        data = pickle.loads(data)
        process = sp.Popen(data, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if stderr == b'':
            output = b'\nOK\n' + stdout
            output = pickle.dumps(output)
            writer.write(output)
            await writer.drain()
        else:
            output = b'\nERROR\n' + stderr
            output = pickle.dumps(output)
            writer.write(output)
            await writer.drain()
        print("PID: %d" % os.getpid())


async def main(PORT):

    server = await asyncio.start_server(
        handle, '192.168.54.109', PORT)

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sv multiconexiones 1 solo proceso asyncio")
    parser.add_argument("-p", "--port", type=int, required=True, help="Ingrese el numero de puerto")
    args = parser.parse_args()
    PORT = args.port
    asyncio.run(main(PORT))