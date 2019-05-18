import time
from celery.task import Task


class MyTask(Task):
    name = 'my-task'  # 定时任务中使用

    def run(self, *args, **kwargs):
        print('start add task...')
        time.sleep(3)
        arg = [str(i) for i in args]
        if kwargs:
            kw = [str(kwargs[j]) for j in kwargs]
            arg.extend(kw)
        print('you entered %s' % ','.join(arg))
        print('end add task...')



