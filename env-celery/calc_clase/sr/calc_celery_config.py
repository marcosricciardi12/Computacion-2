from celery import Celery

app = Celery('calc_celery', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379', include=['calc_celery', 'calc_mensajes'])

