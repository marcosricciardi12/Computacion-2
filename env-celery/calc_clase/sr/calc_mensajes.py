from calc_celery_config import app
import time

@app.task
def saludo():
    time.sleep(5)
    return "hola mundo, celery reportando..."
