from celery import Celery

# 生成Celery对象，指定任务名字
app = Celery('demo')
# 通过Celery实例加载配置文件，直接使用配置文件中定义的属性
app.config_from_object('celery_app.celeryconfig')


