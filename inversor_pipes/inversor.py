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

def invertline(line, r, w, r1, w1, i):
    r[i], w[i] = os.pipe()
    r1[i], w1[i] = os.pipe()
    fpid = fork()
    if fpid == 0:
        os.close(w[i])
        os.close(r1[i])
        r[i] = os.fdopen(r[i])
        linea = r[i].read()
        w1[i] = os.fdopen(w1[i],'w')
        w1[i].write("%s" % linea[::-1])
        w1[i].flush()
        w1[i].close
        os._exit(0)
    else:
        os.close(r[i])
        os.close(w1[i])
        w[i] = os.fdopen(w[i],'w')
        w[i].write("%s" % line)
        w[i].flush()
        w[i].close()

def main():
    parser = argparse.ArgumentParser(description="INVERSOR DE LINEAS.\n Por cada linea que tenga el archivo a leer,"
    " se creeara un proceso hijo, el cual recibirá una linea del archivo leida por el padre desde un pipe, "
    "el proceso hijo invertirá esta linea y la mandará por otro pipe nuevamente al padre. "
    "Finalmente el padre leera todas las lineas invertidas que recibió por cada pipe y lo mostrará por pantalla")
    
    parser.add_argument("-f", "--path", type=str, required=True, help="Ingrese el path del archivo a leer")
    args = parser.parse_args()
    with open(args.path, "r") as file1:
        total_lines = sum(1 for line in file1)
    r = [[] for x in range(total_lines)]
    w = [[] for y in range(total_lines)]
    r1 = [[] for z in range(total_lines)]
    w1 = [[] for w in range(total_lines)]
    file1 = open(args.path, "r")
    count = 0
    for line in file1:
        invertline(line, r, w, r1, w1, count)
        count = count + 1
    for i in range(total_lines):
        r1[i] = os.fdopen(r1[i])
        linea = r1[i].read()
        print("%s" % linea)
        os.wait()
    file1.close()   

if __name__ == '__main__':
    main()