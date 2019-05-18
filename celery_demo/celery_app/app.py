from celery_app.task1 import add
from celery_app.task2 import multi


add.delay(1, 2)
multi.delay(3, 4)
