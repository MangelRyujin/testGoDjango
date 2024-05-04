from django.core.mail import send_mail
from django.conf import settings



def send_email_task(task,email):
    send_mail(
    f'Cambio en la tarea: {task.title}',
    f'Vea el cambio en el siguiente enlace: http://localhost:8000/tasks/{task.id}',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False
)