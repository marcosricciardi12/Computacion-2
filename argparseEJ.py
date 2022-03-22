# Escribir un programa que reciba dos nombres de archivos por línea de órdenes utilizando los parámetros “-i” y “-o” procesados con argparse.

# El programa debe verificar que el archivo pasado a “-i” exista en el disco. De ser así, lo abrirá en modo de solo lectura, leerá su contenido, y copiará dicho contenido en un archivo nuevo cuyo nombre será el pasado a “-o”. Si el archivo nuevo ya existe, deberá sobreescribirlo.

# Ejemplo:
# python3 copiar.py -i existente.txt -o nuevo.txt

import argparse

def main():

    parser = argparse.ArgumentParser(description="Copiar archivo")
    parser.add_argument("-i", "--input", type=str, required=True, help="string")
    parser.add_argument("-o", "--output", type=str, required=True, help="string")
    args = parser.parse_args()

    print('Input %s.' % args.input)
    print('Output %s.' % args.output)

    with open(args.input,"r") as inputfile:
         with open(args.output,"w") as outputfile:
             outputfile.write(inputfile.read())

if __name__ == '__main__':
    main()