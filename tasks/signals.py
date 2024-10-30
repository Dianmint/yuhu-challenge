from django.db.models.signals import post_save, post_delete
from django.template.loader import render_to_string
from django.dispatch import receiver

from .celery_tasks import send_email_task
from .models import Task


@receiver(post_save, sender=Task)
def send_update_notification(sender, instance, created, **kwargs):
    if created:
        subject = "New Task Created"
        message = f"A new task has been created: {instance.title}"
    else:
        subject = "Task Updated"
        message = f"The task '{instance.title}' has been updated."

    html_content = render_to_string("mail_notification.html", {
        "subject": subject,
        "message": message,
        "task": instance,
    })

    recipient_list = [instance.email]
    send_email_task.delay(subject, message, recipient_list, html_content=html_content)

@receiver(post_delete, sender=Task)
def send_task_deletion_notification(sender, instance, **kwargs):
    subject = "Task Deleted"
    message = f"The task '{instance.title}' has been deleted."

    html_content = render_to_string("mail_notification.html", {
        "subject": subject,
        "message": message,
        "task": instance,
    })

    recipient_list = [instance.email]
    send_email_task.delay(subject, message, recipient_list, html_content=html_content)
