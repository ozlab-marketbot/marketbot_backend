from __future__ import absolute_import
import os
from celery import Celery

# settings.py 위치 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Django의 settings.py에서 celery 설정 가져오기
app.config_from_object('django.conf:settings', namespace='CELERY')

# 모든 앱에서 task 모듈 자동 검색
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
