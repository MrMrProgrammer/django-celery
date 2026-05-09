from celery import shared_task


@shared_task(queue="tasks")
def send_email_to_user():
    raise ConnectionError("connection lost ...")
    print("email has been sent to user")
