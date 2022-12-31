from decouple import config
from django.core.mail import send_mail

from config.celery import app


@app.task
def send_lol():
    send_mail(
        'from billal',
        'lol',
        config('EMAIL_HOST_USER'),
        [config('EMAIL_HOST_USER')],
    )
