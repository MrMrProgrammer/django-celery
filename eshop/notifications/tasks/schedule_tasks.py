from config.celery import app
from datetime import timedelta
from celery.schedules import crontab


app.conf.beat_schedule = {
    "task_1": {
        "task": "notifications.tasks.schedule_tasks.task_1",

        # https://crontab.guru
        "schedule": crontab(
            minute="*/1",
            hour="*",
            day_of_week="*",
            day_of_month="*",
            month_of_year="*"
        )
    },
    "task_2": {
        "task": "notifications.tasks.schedule_tasks.task_2",
        "schedule": timedelta(seconds=10)
    },
}


@app.task(queue="tasks")
def task_1():
    return "Running task 1"


@app.task(queue="tasks")
def task_2():
    return "Running task 2"
