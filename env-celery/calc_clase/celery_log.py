
"""
Funciones de logging y mensajeria
"""
import time
from celery_calc_config import app

@app.task
def saludo():
    time.sleep(5)
    return "Hola Mundo, calculadora reportandose..."
