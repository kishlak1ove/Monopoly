from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ваш_проект.settings')  # Замените «ваш_проект» на название вашего проектного пакета.

app = Celery('ваш_проект')  # Замените на название вашего проектного пакета.

# Настройки из Django конфигурации
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загружайте модули задач из всех зарегистрированных Django приложений.
app.autodiscover_tasks()