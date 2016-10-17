# Creates flask and rabbit server for the celery workers to connect
# By Andrea Rylander, Alessandro Piccolo & Abdullah Al Hinai
import os
import time

from flask import Flask
from flask import url_for

from celery import Celery
from celery.result import AsyncResult
import celery.states as states
from celery_tasks import benchmark
# Creates celery worker
env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL','amqp://group_11:wearegroup_11@localhost/group_11_vhost'),
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND','amqp://')

celery = Celery('tasks',
                broker = CELERY_BROKER_URL,
                backend = CELERY_RESULT_BACKEND)

# Creating the flask app, light weight webb framework
app = Flask(__name__)

# Lists of problem (Different variables (see table.m))
#problems = ['prob1.m','prob2.m','prob3.m']


# Store the reulsts, execution time and relative error
allResults = []

# Enables user to ping flaskto send an request to the rabbit queue
# We get x number of tasks depending on the number of problems definied
# in list variable "problem"
@app.route('/benchmark',methods = ['GET'])
def start_benchmark_task():
    #start_time = time.time()
    # Sends tasks (request) to rabbit
    #for problem_name in problems:
    problem_to_sovle = 1
    results = celery.send_task('celery_tasks.benchmark' args = [problem_to_solve]) # results is a list
    allResults.append(results)
    #print (problem_name + " \nThe times:\n %s, \n\n The relative errors:\n %s \n" % (results))
    #print("---Execution time %s seconds ---" % (time.time() - start_time))
    #return str(allResults)

if(__name__ == '__main__'):
    app.run(host = '0.0.0.0', debug = True)
