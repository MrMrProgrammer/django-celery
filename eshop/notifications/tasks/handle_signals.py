from config.celery import app
import sys
from celery.signals import task_failure


@app.task(queue="tasks")
def my_tasks():
    raise ValueError("Task failed")


@app.task(queue="tasks")
def error_handle_task(task_id):
    sys.stdout.write(f"Task id is {task_id}")


@task_failure.connect(sender=my_tasks)
def handle_my_task_failure(sender=None, task_id=None, **kwargs):
    error_handle_task.delay(task_id)


def run_task():
    my_tasks.delay()
