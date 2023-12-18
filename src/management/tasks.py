from celery import shared_task


@shared_task
def my_tasks():
    print("0")
    return 0
