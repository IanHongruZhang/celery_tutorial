from celery import platforms
platforms.C_FORCE_ROOT = True

BROKER_URL = 'redis://127.0.0.1:6379/2'    # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/3'    # 指定 Backend

CELERY_IMPORTS = {
	'celery_app.crawler1',
	'celery_app.crawler2'
}