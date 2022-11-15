import os
import sys
import signal
def grabar(pid_bot):
    print("Me grabe manso audio")
    with open("grabacion.txt", "a") as grabacion:
        sys.stdin = open(0)
        data = input("Ingrese texto a grabar: ")
        grabacion.write(data)
    os.kill(pid_bot, signal.SIGUSR1)