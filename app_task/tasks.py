from celery import shared_task
from datetime import datetime
@shared_task
def print_hello_everysec():
    print("Hello world", datetime.now())