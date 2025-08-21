import logging

from celery import Celery
from kombu import Queue, Exchange

import app.celery.celeryconfig as celeryconfig
from app.celery.celeryconfig import long_task


# logging.basicConfig(
#     format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
#     datefmt="%m-%d %H:%M",
#     handlers=[
#         logging.FileHandler("flask_celery_redis_celery_worker.log"),
#         logging.StreamHandler(),
#     ],
# )


celery_app = Celery()
celery_app.config_from_object(celeryconfig)
celery_app.conf.task_queues = (
    Queue(
        name=long_task,
        exchange=Exchange(long_task),
        routing_key=long_task,
    ),
)