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
problems = range(1, 2) #range(1, 7) # List, for python 3.x: list(range(1, 7))

# Enables user to ping flaskto send an request to the rabbit queue
# We get x number of tasks depending on the number of problems definied
# in list variable "problem"
@app.route('/benchmark',methods = ['GET'])
def start_benchmark_task():
    #start_time = time.time()
    # Store the reulsts, name of solver, execution time and relative error
    all_results = {}
    # rs = ResultSet([])
    # Sends tasks (request) to rabbit
    #for problem_to_solve in problems:
        #all_results.update(celery.send_task('celery_tasks.benchmark', args = [problem_to_solve]))
        #rs.add(benchmark.delay(problem_to_solve))
    #herp = group(benchmark.delay(problem_to_solve) for problem_to_solve in problems).get()
    #g = group(benchmark.s(1), benchmark.s(2))
    g = group(benchmark.s(problem_to_solve) for problem_to_solve in problems)
    g.apply_async()
    herp = g() 
    print herp.get()  #we can print it directly 
    result_maybe = herp.get()
    print ('results_maybe = %s, type = %s' %(result_maybe, type(result_maybe) ))
    #print (problem_name + " \nThe times:\n %s, \n\n The relative errors:\n %s \n" % (results))
    #print("---Execution time %s seconds ---" % (time.time() - start_time))
    return render_template('index.html', result_maybe=result_maybe)

if(__name__ == '__main__'):
    app.run(host = '0.0.0.0', debug = True)
