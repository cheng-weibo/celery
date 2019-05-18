import time
from celery_app import app


@app.task
def multi(x, y):
    time.sleep(5)
    print('--------multi------')
    return x * y
