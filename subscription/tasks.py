from Newsletter.celery import celery_app
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Subscriber


@celery_app.task(name="send_weeky_updates")
def send_weeky_email():
    email_list = [subscriber.email for subscriber in Subscriber.objects.all()]
    html_content = render_to_string("subscription/mail.html", {})

    mail = EmailMessage(
        subject="Backend Weekly Update",
        body=html_content,
        to=email_list,
        headers={"Message-ID": "224"}
    )
    mail.content_subtype = "html"
    mail.send(fail_silently=False)


@celery_app.task(name="send_new_subscriber_notification")
def send_new_subscriber_notification():
    pass
