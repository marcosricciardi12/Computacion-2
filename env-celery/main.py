import calc_mat
import argparse 
def func_calc(matriz, op):
    result = []
    linea_result = []
    for linea in matriz:
        linea_result = []
        for elemento in linea:
            if(op == 'raiz'):
               resultado = calc_mat.raiz.delay(int(elemento))
            if(op == 'pot'):
                resultado = calc_mat.pot.delay(int(elemento))
            if(op == 'log'):
                resultado = calc_mat.log_d.delay(int(elemento))
            linea_result.append(resultado.get())
        result.append(linea_result)
    return result

def main():
    matrix = []
    parser = argparse.ArgumentParser(description="-f Directorio del archivo a leer, -c funcion a ingresar: raiz, pot, log")
    parser.add_argument("-f", "--inputfile", type=str, required=True, help="string")
    parser.add_argument("-c", "--calc", type=str, required=True, help="string")
    args = parser.parse_args()
    inputfile = args.inputfile
    calc_op = args.calc

    if not (args.calc == 'pot' or args.calc == 'raiz' or args.calc == 'log'):
        print("Función no valida")
        os._exit(0)
    
    with open(args.inputfile, "r") as inputfile:
        for line in inputfile:
            matrix.append(line[:-1].split(' '))
    print("\n")
    for linea in matrix:
        print(linea)
    print("\n")
    resultado = func_calc(matrix, calc_op)

    for linea in resultado:
        print(linea)

if __name__ == '__main__':
    main()