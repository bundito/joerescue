from celery import Celery

app = Celery('tasks', broker='pyampq://ampq@localhost//')

@app_task
def add(x, y):
    return x + y

