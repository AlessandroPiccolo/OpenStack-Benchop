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
#Making time into normal array and then "flattining"
@celery.task(name = 'celery_tasks.benchmark')
def benchmark(problem_to_solve):
        time, relerr, filepaths = octave.tablee(problem_to_solve)
	timearray = [item for sublist in time.tolist() for item in sublist]
	relerrarray = [item for sublist in relerr.tolist() for time in sublist]
	#print("time: %s, type = %s " %(timearray, type(timearray)))
        #print("relative error: %s type = %s" %(relerrarray, type(relerrarray) ))
        #print("filepaths %s, type = %s" %(filepaths, type(filepaths) ))
        #print([time, relerr, filepaths])
        return 1

