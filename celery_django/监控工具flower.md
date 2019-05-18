pip install flower

celery flower --address=0.0.0.0 --port=5555
    --broker=xxx --basic_auth=aaa:aaa

http://localhost:5555 ==> flower默认地址
broker: flower默认使用rabbitmq, 可以broker设置为redis的地址
basic_auth:  不想让别人访问该服务的话使用basic auth认证

使用###python manage.py celery flower###启动flower则会读celery配置
