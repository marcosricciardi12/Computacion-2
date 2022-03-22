import getopt
import sys


# Crear una calculadora, donde se pase como argumentos luego de la opción -o el operador que se va a ejecutar (+,-,*,/), luego de -n el primer número de la operación, y de -m el segundo número.

# Ejemplo:
# python3 calc.py -o + -n 5 -m 6
# 5 + 6 = 11

def main():
    o = ''
    n = ''
    m = ''
    (opt, arg) = getopt.getopt(sys.argv[1:], 'o:n:m:', ["operador=", "numero1=", "numero2="])
    print("Opciones: ", opt)
    print("Argumentos: ", arg)

    for (op, ar) in opt:
        if op in ['-o', '-n', '-m', "--operador", "--numero1", "--numero2"]:
            if op == '-o' or op == '--operador':
                o = ar
            elif op == '-n' or op == '--numero1':
                n = ar
            elif op == '-m' or op == '--numero2':
                m = ar
            else:
                print("Opcion invalida")
    n = float(n)
    m = float(m)
    print(o)
    print(n)
    print(m)

    if o == '+' or o == '-' or o == '/' or o == '*':
        operacion = str(n)+ ' ' + o + ' ' + str(m)
        print("La operacion a resolver es: ", operacion)
        print("El resultado es", str(eval(operacion)))

             

if __name__ == '__main__':
    main()