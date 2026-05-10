# from celery import shared_task
from config.celery import app
import time


# @shared_task(queue="tasks")
# def send_email_to_user():
#     raise ConnectionError("connection lost ...")
#     print("email has been sent to user")


@app.task(queue="tasks", time_limit=10)
def send_email_to_user():
    time.sleep(6)
    return "Email has been sent to user successfully"


def send_email():
    result = send_email_to_user.delay()

    try:
        task_result = result.get(timeout=4)

    except TimeoutError:
        print("Task timed out")
        # result.revoke(terminate=True)
