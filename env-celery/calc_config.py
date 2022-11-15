from celery import Celery

app = Celery(   'calc_mat', 
                broker= 'redis://localhost:6379', 
                backend = 'redis://localhost:6379', 
                include = ['calc_mat'])
                