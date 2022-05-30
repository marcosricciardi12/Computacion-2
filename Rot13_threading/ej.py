# Escribir un programa que genere dos hilos utilizando threading.

# Uno de los hilos deberá leer desde stdin texto introducido por el usuario, y deberá escribirlo en un mecanismo IPC (*).

# El segundo hijo deberá leer desde dicho mecanismo IPC el contenido de texto, lo encriptará utilizando el algoritmo ROT13, y lo almacenará en una cola de mensajes (queue).

# El primer hijo deberá leer desde dicha cola de mensajes y mostrar el contenido cifrado por pantalla.

# (*) Verificar si el uso de os.pipe(), named pipes, o multiprocessing.Pipe() son thread-safe, caso contrario usar Queue.
import multiprocessing as mp
import sys, threading
from rot13 import rot13_func

def hijo_lector_stdin(w, q):
    print("Hijo solicita mensaje para escribir en el pipe")
    sys.stdin = open(0)
    data_input = sys.stdin.readline()
    w.send(data_input)
    w.close()
    print("El mensaje encriptado es: %s" % q.get())   

def hijo_lector_pipe_cola(r, q):
    print("Hijo esperando leer del pipe")
    data_input = r.recv()
    print("Hijo leyó del pipe: %s" % str(data_input))
    r.close()
    mensaje_encriptado = rot13_func(str(data_input))
    q.put(mensaje_encriptado)    

if __name__ == '__main__':
    r, w = mp.Pipe()
    q = mp.Queue()
    thread1 = threading.Thread(target = hijo_lector_stdin, args=(w, q))
    thread2 = threading.Thread(target = hijo_lector_pipe_cola, args=(r, q))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()