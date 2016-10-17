# Creates celery worker and defines the benchmark task to do
import os
from celery import Celery
from oct2py import octave

env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL','amqp://group_11:wearegrup_11@localhost/group_11_vhost'),
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND','amqp://')

celery = Celery('tasks',
                broker = CELERY_BROKER_URL,
                backend = CELERY_RESULT_BACKEND)

# Run octave benchmark test for a specific problem (enviroment)
@celery.task(name = 'celery_tasks.benchmark')
def benchmark(problemName):
        octave.run(problemName)
        return octave.timeBSeuCallUI(), octave.relerrBSeuCallUI()

