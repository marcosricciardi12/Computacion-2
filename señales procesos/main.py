import multiprocessing as mp
import signal
import os
import sys
import subprocess as sp
from telegram import telegram_bot
from record import grabar

def main():
    grabando = False
    bot_telegram = mp.Process(target = telegram_bot)
    bot_telegram.start()
    print("bot_telegram iniciado: PID %d" % bot_telegram.pid)

    print("Soy el proceso PADRE PID: %d" % os.getpid())
    while True:
        data = input("presione enter(Main PADRE): ")
        if data == 'a':
            grabacion = mp.Process(target= grabar, args=(bot_telegram.pid, ))
            grabacion.start()
            grabando = True
        if grabando:
            grabacion.join()
            grabando = False


    bot_telegram.join()


if __name__ == '__main__':
    main()
