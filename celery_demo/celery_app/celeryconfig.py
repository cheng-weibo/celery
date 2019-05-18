from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://:123123@localhost:6379/1'  # broker

CELERY_RESULT_BACKEND = 'redis://:123123@localhost:6379/2'  # backend

CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {  # 定时任务的名字
        'task': 'celery_app.task1.add',  # 执行的任务
        'schedule': timedelta(seconds=20),  # 每20秒执行
        'args': (2, 3)
    },
    'task2': {
        'task': 'celery_app.task2.multi',
        'schedule': crontab(hour=16, minute=49),  # 每天定时执行
        'args': (2, 3)
    }
}



