# Escribir un programa que reciba por argumento la opción -f acompañada de un path_file.

# Etapa 1:
# El programa deberá crear un segmento de memoria compartida anónima, y generar dos hijos: H1 y H2

# El H1 leerá desde el stdin línea por línea lo que ingrese el usuario.

# Cada vez que el usuario ingrese una línea, H1 la almacenará en el segmento de memoria compartida, y enviará la señal USR1 al proceso padre.

# El proceso padre, en el momento en que reciba la señal USR1 deberá mostrar por pantalla el contenido de la línea ingresada por el H1 en la memoria compartida, y deberá notificar al H2 usando la señal USR1.

# El H2 al recibir la señal USR1 leerá la línea desde la memoria compartida la línea, y la almacenará en mayúsculas en el archivo pasado por argumento (path_file).

# Etapa 2:
# Cuando el usuario introduzca "bye" por terminal, el hijo H1 enviará la señal USR2 al padre indicando que va a terminar, y terminará.
# El padre, al recibir la señal USR2 la enviará al H2, que al recibirla terminará también.
# El padre esperará a que ambos hijos hayan terminado, y terminará también.



import argparse, os, mmap, sys, signal

def hijo2_terminar(nro, frame): #Cuando el hijo2 recibe la señal SIGUSR2 del padre, simplemente termina el hijo2
    print("Soy el hijo2 PID: %d     recibi la señal de terminar. Terminando..." % os.getpid())
    os._exit(0)


def hijo1_avisa_al_padre(nro, frame): #Padre recibe señal SIGUSR2 desde hijo 1 el cual le avisa que va a terminar
    print("Proceso padre PID: %d      Mi hijo1 PID: %d va a terminar" % (os.getpid(), hijo1))
    os.kill(hijo2, signal.SIGUSR2) #El padre envia la señal SIGUSR2 al hijo2 el cual correra el manejador hijo2_terminar
    signal.signal(signal.SIGUSR1, signal.SIG_DFL) #Finalmente el padre cambia el comportamiento de la señal SIGUSR1 a su comp

def padre_lee_hijo1_y_notifica_hijodos(nro, frame): #Manejador donde el padre es notificado por hijo1 y lee la mem compartida
    shared_mem.seek(0) #Padre se posiciona al principio de la memoria compartida
    leer = shared_mem.readline() #Padre lee memoria compartida
    print("(PID %d) Linea leida: %s" % (os.getpid(),leer.decode())) #El padre muesrtra por pantalla la linea leida de la memoria compartida, que fue escrita por el hijo1
    os.kill(hijo2, signal.SIGUSR1)# El padre envia la señal SIGUSR1 al hijo2 en la cual notifica que ya leyó la memoria compartida

def hijo2_notificado(nro, frame): #Hjo 2 recibe la seña SIGUSR1 y corre este manejador
    shared_mem.seek(0) #Hijo 2 va al principio de la mem compartida
    leer = shared_mem.readline().decode().upper().encode() #Hijo 2 consume los datos de la memoria compartida, lo decodifica, pasa a mayus y lo vuelve a codificar
    print("(PID %d) Linea en mayus: %s" % (os.getpid(), (leer.decode()))) #Hijo 2 imprime por pantalla la linea leida en MAYUS
    file.write(leer) #EL hijo2 escribe en el archivo indicado por comando la linea leida por teclado en mayus
    file.flush() #Hijo 2 limpia el buffer de escritura del archivo abierto

def main():
    print("PID Padre: %d" % os.getpid())
    signal.signal(signal.SIGUSR1, padre_lee_hijo1_y_notifica_hijodos) #Cambio señal SIGUSR1 para que el padre al recibir esta señal, ejecute al manenejador y
    # lea lo que hizo el hijo 1 y notifica al hijo 2
    signal.signal(signal.SIGUSR2, hijo1_avisa_al_padre) #Cambio señal SIGUSR2 para que el hijo1 al recibir esta señal, ejecute al manenejador y
    # le avise al padre que va a terminar (el hijo1 le manda esta señal al padre y el padre ejecuta el manejador notificando que su hijo va a terminar
    # )
    #Hijo1
    global hijo1
    hijo1 = os.fork() # creo al hijo 1
    #bloque donde el hijo 1 corre su proceso
    if not hijo1:
        file.close()
        print("(Proceso Hijo 1 PID %d) Ingrese linea por teclado: " % os.getpid())
        for line in sys.stdin: #Hijo 1 lee el standar input
            if line == "bye\n": #Si la linea ingresada es bye: 
                print("Ingresaste bye... terminando procesos")
                os.kill(os.getppid(), signal.SIGUSR2) #el proceso hijo1 manda una señal SIGUSR2 al padre
                break #El proceso hijo sale del bucle for y sigue en el print, posterioro a eso, termina el proceso Hijo1
            #la linea ingresada no es bye:
            shared_mem.resize(len(line)) # Se calcula en bytes el tamaño de la cadena ingresada por teclado y se redimensona el buffer de la mem compartida
            shared_mem.seek(0) # Me ubico en la posicion 0 de la memoria compartida
            shared_mem.write(line.encode()) #Escribe el hijo1 en la memoria compartida la linea ingresada por teclado
            shared_mem.seek(0) #Dejo la memoria compartida en la posicion inicial
            os.kill(os.getppid(), signal.SIGUSR1) #El hijo1 le manda la señal SIGUSR1 Al padre, con la cual notifica que hijo1 escribio la memoria compartida y padre debe leerla
            print("Ingrese linea por teclado: ")
        print("Proceo hijo1 PID %d saliendo" % os.getpid())
        os._exit(0) #Termina el hijo1
        
    #Hijo2
    global hijo2
    hijo2 = os.fork() #Se crea el hijo 2
    
    if not hijo2: #Bloque que corre el hijo2
        signal.signal(signal.SIGUSR1, hijo2_notificado) # El hijo 2 cambia el comportamiento de que hacer cuando recibe la señal SIGUSR1
        signal.signal(signal.SIGUSR2, hijo2_terminar) # El hijo 2 cambia el comportamiento de que hacer cuando recibe la señal SIGUSR2
        while True: #En forma de bucle el hijo 2 queda esperando un señal por cada vez que el hijo 1 escriba la memoria compartida
            signal.pause()
        os._exit(0)

    #Padre
    args = 0
    # signal.pause()
    # print("Padre PID %d esperando para terminar.." % os.getpid())
    os.wait()
    os.wait() 
    print("Padre PID %d Saliendo" % os.getpid())

shared_mem = mmap.mmap(-1,1024)
parser = argparse.ArgumentParser(description="Falta descripcion")
parser.add_argument("-f", "--path", type=str, required=True, help="Ingrese el path del archivo a leer")
args = parser.parse_args()
hijo1 = 0
hijo2 = 0
file = open(args.path, 'wb')

if __name__ == '__main__':
    main()