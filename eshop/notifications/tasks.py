from celery import shared_task, group, chain
import time
import logging


# @shared_task(rate_limit="1/m")
# def task_1(queue="celery"):
#     time.sleep(3)
#     return


# @shared_task
# def task_2(queue="celery:1"):
#     time.sleep(3)
#     return


# @shared_task
# def task_3(queue="celery:2"):
#     time.sleep(3)
#     return


# @shared_task
# def task_4(queue="celery:3"):
#     time.sleep(3)
#     return


# group_tasks = group(
#     task_1.s(),
#     task_2.s(),
#     task_3.s(),
#     task_4.s()
# )
# group_tasks.apply_async()


# chain_tasks = chain(
#     task_1.s(),
#     task_2.s(),
#     task_3.s(),
#     task_4.s()
# )
# chain_tasks.apply_async()


# @shared_task(queue="tasks")
# def send_sms_to_user():
#     time.sleep(3)
#     print("sms has been sent")


@shared_task(queue="tasks")
def my_task():
    try:
        print("this is my task")
        raise ValueError("value is not valid")
    except Exception as e:
        logging.error(f"an exception has been occurred. {e}")
        raise ConnectionError("connection error occurred")
