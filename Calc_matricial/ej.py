# Realizar un programa en python que reciba por argumentos:

# -p cantidad_procesos

# -f /ruta/al/archivo_matriz.txt

# -c funcion_calculo
# El programa deberá leer una matriz almacenada en el archivo de texto pasado por argumento -f, y deberá calcular la funcion_calculo para cada uno de sus elementos.

# Para aumentar la performance, el programa utilizará un Pool de procesos, y cada proceso del pool realizará los cálculos sobre una de las filas de la matriz.

# La funcion_calculo podrá ser una de las siguientes:

# raiz: calcula la raíz cuadrada del elemento.
# pot: calcula la potencia del elemento elevado a si mismo.
# log: calcula el logaritmo decimal de cada elemento.
# Ejemplo de uso:
# Suponiendo que el archivo /tmp/matriz.txt tenga este contenido:

# 1, 2, 3
# 4, 5, 6
# python3 calculo_matriz -f /tmp/matriz.txt -p 4 -c pot
# 1, 4, 9
# 16, 25, 36
import argparse
from ast import Global
import sys
import time
import subprocess as sp
import multiprocessing as mp
import os
import math

matrix = []
global args
def func_calc(linea):
    global args
    if len(linea)>4:
        time.sleep(3)
    linea_calc = []
    if args.calc == 'pot':
        for element in linea:
            linea_calc.append(math.pow(int(element), int(element)))
        print(linea_calc)
    elif args.calc == 'raiz':
        for element in linea:
            linea_calc.append(math.sqrt(int(element)))
        print(linea_calc)
    elif args.calc == 'log':
        for element in linea:
            linea_calc.append(math.log10(int(element)))
        print(linea_calc)
    print("PID Proceso padre desde hijo: %d" % os.getppid())
    return linea_calc

def main():

    parser = argparse.ArgumentParser(description="-p Cantidad de procesos, -f Directorio del archivo a leer, -c funcion a ingresar: raiz, pot, log")

    parser.add_argument("-p", "--process", type=int, required=True, help="string")
    parser.add_argument("-f", "--inputfile", type=str, required=True, help="string")
    parser.add_argument("-c", "--calc", type=str, required=True, help="string")
    global args
    args = parser.parse_args()

    print('Command: %d' % args.process)
    print('Output File: %s' % args.inputfile)
    print('Log File: %s' % args.calc)
    if not (args.calc == 'pot' or args.calc == 'raiz' or args.calc == 'log'):
        print("Función no valida")
        os._exit(0)

    print("PID Proceso padre main: %d" % os.getpid())
    with open(args.inputfile, "r") as inputfile:
        for line in inputfile:
            matrix.append(line[:-1].split(' '))

    pul = mp.Pool(processes = int(args.process))

    results=[]
    results = pul.map_async(func_calc,matrix).get()
    print("espereando...")
    for line in results:
        print(line)

if __name__ == '__main__':
    main()