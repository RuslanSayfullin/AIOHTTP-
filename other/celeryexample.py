from celery import Celery
from Django.core.mail import send_mail

app = Celery('send_mail', broken = 'pyamqp://guest@localhost//')

@app.task
def send_email_task():
    send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
    )
    return 'Email sent successfully'
