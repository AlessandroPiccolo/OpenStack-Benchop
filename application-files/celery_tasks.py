# Creates celery worker and defines the benchmark task to do
import os
from celery import Celery
from oct2py import octave

env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL','amqp://group_11:wearegroup_11@localhost/group_11_vhost'),
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND','amqp://')

celery = Celery('tasks',
                broker = CELERY_BROKER_URL,
                backend = CELERY_RESULT_BACKEND)

# Run octave benchmark test for a specific problem (enviroment), returns list of time and rel error
@celery.task(name = 'celery_tasks.benchmark')
def benchmark(problem_to_solve):
        time, relerr, filepathsBSeuCallUI = octave.table(problem_to_solve)
        print("time: %s, type = %s " %(time, type(time) ))
        print("relative error: %s type = %s" %(relerr, type(relerr) ))
        print("filepaths %s, type = %s" %(filepathsBSeuCallUI, type(filepathsBSeuCallUI) ))
        #print([time, relerr, filepathsBSeuCallUI])
        return 1

