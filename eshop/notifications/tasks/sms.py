from config.celery import app


@app.task(
    queue="tasks",
    autoretry_for=(ConnectionError,),
    default_retry_delay=5,
    retry_kwargs={"max_retries": 5}
)
def send_sms_to_user():
    raise ConnectionError("Connection Error ...")
    # print("sms has been sent to user")
