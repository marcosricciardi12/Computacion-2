import os
import signal

def leer_grabacion(nro, framw):
    with open("grabacion.txt", "r") as grabacion:
        print("El bot de telegram leyo y envio la grabacion: %s" % grabacion.read())
        print("PID BOT TELEGRAM: %d" % os.getpid())

def telegram_bot():
    signal.signal(signal.SIGUSR1, leer_grabacion)
    while True:
        pass