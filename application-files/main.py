# Creates flask and rabbit server for the celery workers to connect
# By Andrea Rylander, Alessandro Piccolo & Abdullah Al Hinai
import os
import time

from flask import Flask
#from flask import url_for

from celery import Celery
#from celery.result import AsyncResult
#import celery.states as states
from celery import group
from celery_tasks import benchmark
from flask import Markup
from flask import render_template
# Creates celery worker
env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL','amqp://group_11:wearegroup_11@localhost/group_11_vhost')
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND','amqp://')

celery = Celery('tasks',
                broker = CELERY_BROKER_URL,
                backend = CELERY_RESULT_BACKEND)

# Creating the flask app, light weight webb framework
app = Flask(__name__)

# Solve problems 1-6 (we are going to get 6 different tasks)
problems = range(1, 4) # List, for python 3.x: list(range(1, 7))

# Enables user to ping flask to send an request to the rabbit queue
# We get x number of tasks depending on the number of problems definied
# in list variable "problem"
@app.route('/benchmark/<sig>',methods = ['GET'])
def start_benchmark_task(sig):
    # Creates all tasks and puts them in queue. get() makes this function wait untill all tasks are completed
    # All output from the tasks are going to be appended in our results variable (it is a long list)
    results = group(benchmark.s(problem_to_solve,sig) for problem_to_solve in problems)().get()
    return render_template('index.html', results=results)

if(__name__ == '__main__'):
    app.run(host = '0.0.0.0', debug = True)
