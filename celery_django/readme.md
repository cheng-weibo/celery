pip install django-celery  4.0以上只支持django1.8以上

INSTALLED_APPS添加djcelery
添加其他app时只添加app名字，不要定位到AppConfig

启动celery
###  python manage.py celery worker -l info
启动celery beat
###  python manage.py celery beat -l info
python manage.py celery worker -Q queue   ???


项目同名目录创建celeryconfig.py

app下创建任务文件tasks.py， from celery.task import Task
继承Task创建类MyTask，实现run方法，run方法中定义任务

    调用时先实例化MyTask，调用delay
    t = MyTask()
    t.delay(1, 2, a=3, b=4)

