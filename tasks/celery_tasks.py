from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def send_email_task(subject, message, recipient_list, html_content=None):  
    from_email = settings.EMAIL_HOST_USER
    
    if html_content:
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html") 
    else:
        email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
    
    email.send()
