# Escribir un programa en Python que reciba los siguientes argumentos por línea de comandos:

# -n <N>
# -r <R>
# -h
# -f <ruta_archivo>
# -v
# El programa deberá abrir (crear si no existe) un archivo de texto cuyo path ha sido pasado por argumento con -f.

# El programa debe generar <N> procesos hijos. Cada proceso estará asociado a una letra del alfabeto (el primer proceso con la "A", el segundo con la "B", etc). 
# Cada proceso almacenará en el archivo su letra <R> veces con un delay de un segundo entre escritura y escritura (realizar flush() luego de cada escritura).

# El proceso padre debe esperar a que los hijos terminen, luego de lo cual deberá leer el contenido del archivo y mostrarlo por pantalla.

# La opción -h mostrará ayuda. La opción -v activará el modo verboso, en el que se mostrará antes de escribir cada letra en el archivo: 
    #   Proceso <PID> escribiendo letra 'X'.

# Ejemplo 1:
# ./escritores.py -n 3 -r 4 -f /tmp/letras.txt

# ABCACBABCBAC
# Ejemplo 2:
# ./escritores.py -n 3 -r 5 -f /tmp/letras.txt -v
# Proceso 401707 escribiendo letra 'A'
# Proceso 401708 escribiendo letra 'B'
# Proceso 401709 escribiendo letra 'C'
# Proceso 401708 escribiendo letra 'B'
# Proceso 401707 escribiendo letra 'A'
# Proceso 401709 escribiendo letra 'C'
# Proceso 401707 escribiendo letra 'A'
# Proceso 401708 escribiendo letra 'B'
# Proceso 401709 escribiendo letra 'C'
# Proceso 401707 escribiendo letra 'A'
# Proceso 401708 escribiendo letra 'B'
# Proceso 401709 escribiendo letra 'C'
# Proceso 401707 escribiendo letra 'A'
# Proceso 401708 escribiendo letra 'B'
# Proceso 401709 escribiendo letra 'C'
# ABCBACABCABCABC

import argparse
import sys
import time
import subprocess as sp
import os
from os import fork
from click import command
from numpy import number

def create_and_calculate(number, letters, alphabet, len_alphabet, file, verbose):
    for i in range(number):
        pos = i % len_alphabet
        letra = alphabet[pos]
        fpid = fork()
        if fpid == 0:
            pid = os.getpid()
            for k in range(letters):
                if verbose:
                    print("Proceso %d escribiendo letra '%s'" % (pid, letra))
                file.write(letra)
                file.flush()
                time.sleep(1)
            os._exit(0)

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    len_alphabet = len(alphabet)
    parser = argparse.ArgumentParser(description="sdasdas")
    parser.add_argument("-n", "--number", type=int, required=True, help="Ingrese el numero de procesos a crear")
    parser.add_argument("-r", "--letters", type=int, required=True, help="Ingrese el numero letras a escribir por proceso")
    parser.add_argument("-f", "--path", type=str, required=True, help="Ingrese el path del archivo a escribir/crear")
    parser.add_argument("-v", "--verbose", action='store_true', help="Ejecutar programa en modo verboso")
    args = parser.parse_args()
    file1 = open(args.path, "w+")
    create_and_calculate(args.number, args.letters, alphabet, len_alphabet, file1, args.verbose)
    for i in range(args.number):
        os.wait()
    file1.seek(0)
    print(file1.read())
    file1.close()   

if __name__ == '__main__':
    main()