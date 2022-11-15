from calc_config import app
from math import log

@app.task
def raiz(a):
    return a**0.5

@app.task
def pot(a):
    return a**a

@app.task
def log_d(a):
    return log(a, 10)