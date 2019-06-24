from celery import Celery

app = Celery("demo") #实例化一个Celery App
app.config_from_object('celery_app.celeryconfig') #加载该app中的配置模块
