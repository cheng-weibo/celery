from celery import Celery

# broker: 消息中间件
# backend：存储任务执行的结果
# 当redis需要密码时-->":密码@"， :123123@
broker = 'redis://:123123@localhost:6379/1'
backend = 'redis://:123123@localhost:6379/2'
app = Celery('my_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    import time
    time.sleep(5)
    return x + y
