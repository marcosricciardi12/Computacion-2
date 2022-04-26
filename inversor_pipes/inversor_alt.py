# Escriba un programa que abra un archvo de texto pasado por argumento utilizando el modificador -f.

# El programa deberá generar tantos procesos hijos como líneas tenga el archivo de texto.
# El programa deberá enviarle, vía pipes (os.pipe()), cada línea del archivo a un hijo.
# Cada hijo deberá invertir el orden de las letras de la línea recibida, y se lo enviará al proceso padre nuevamente, también usando os.pipe().
# El proceso padre deberá esperar a que terminen todos los hijos, y mostrará por pantalla las líneas invertidas que recibió por pipe.
# Ejemplo:
# Contenido del archivo /tmp/texto.txt

# Hola Mundo
# que tal
# este es un archivo
# de ejemplo.
# Ejecución:
# python3 inversor.py -f /tmp/texto.txt
# ovihcra nu se etse
# .olpmeje ed
# lat euq
# odnuM aloH

import argparse
import sys
import time
import subprocess as sp
import os
from os import fork
from click import command
from numpy import number
    

def main():
    parser = argparse.ArgumentParser(description="INVERSOR DE LINEAS.\n Por cada linea que tenga el archivo a leer,"
    " se creeara un proceso hijo, el cual recibirá una linea del archivo leida por el padre desde un pipe, "
    "el proceso hijo invertirá esta linea y la mandará por otro pipe nuevamente al padre. "
    "Finalmente el padre leera todas las lineas invertidas que recibió por cada pipe y lo mostrará por pantalla")
    
    parser.add_argument("-f", "--path", type=str, required=True, help="Ingrese el path del archivo a leer")
    args = parser.parse_args()
    with open(args.path, "r") as file1:
        total_lines = sum(1 for line in file1)
    file1 = open(args.path, "r")
    count = 0
    r, w = os.pipe()
    r1, w1 = os.pipe()
    for i in range(total_lines):
        fpid = fork()
        if fpid == 0:
            os.close(w)
            os.close(r1)
            r = os.fdopen(r)
            linea = r.read()
            w1 = os.fdopen(w1,'w')
            w1.write("%s" % linea[::-1])
            w1.flush()
            w1.close()
            os._exit(0)

    w = os.fdopen(w, 'w')
    for lines in file1:
        w.write(lines)
    w.close()
    os.close(w1)
    r1 = os.fdopen(r1)
    for i in range(total_lines):
        linea = r1.read()
        print("%s" % linea)
        os.wait()
    r1.close()
    file1.close()   

if __name__ == '__main__':
    main()