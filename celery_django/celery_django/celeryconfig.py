import djcelery
from datetime import timedelta
from celery.schedules import crontab
# from djcelery.loaders import DjangoLoader -- setup_loader
djcelery.setup_loader()  # celery使用django settings
BROKER_BACKEND = 'redis'  # 使用redis
BROKER_URL = 'redis://:123123@localhost:6379/1'  # broker
CELERY_RESULT_BACKEND = 'redis://:123123@localhost:6379/2'  # backend

# 默认只有一个queue，所有任务都在一个队列中
# 可以设置多个队列
CELERY_QUEUES = {
    'beat_tasks': {  # 放定时任务的队列
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks',
    },
    'work_queue': {  # 放普通任务的队列
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks',
    },
}
CELERY_DEFAULT_QUEUE = 'work_queue'  # 默认队列

CELERY_IMPORTS = (
    'app01.tasks',
)

# ********有些情况下可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置worker并发数
CELERY_CONCURRENCY = 4

# 允许任务失败后重试
CELERY_ACKS_LATE = True

# **********每个worker最多执行100任务被销毁，可以防止内存泄漏
CELERY_MAX_TASKS_PER_CHILD = 100

# 超时时间，秒，单个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 6*60


# *************定时任务*************
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'my-task',  # 实例化Task类时定义的name， 或者定位到MyTask
        'schedule': timedelta(seconds=20),  # 每20秒执行
        'args': (2, 3),
        'options': {  # 指定任务队列
            'queue': 'beat_tasks'
        },
    },
}


