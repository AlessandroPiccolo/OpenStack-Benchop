# Creates flask and rabbit server for the celery workers to connect
# By Andrea Rylander, Alessandro Piccolo & Abdullah Al Hinai
import os
import time

from flask import Flask
from flask import Markup
from flask import render_template

from celery import Celery
from celery import group
from celery_tasks import benchmark

import pygal

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
@app.route('/benchmark/<float:sig>',defaults={'sig': 0.15}, methods = ['GET'])
def start_benchmark_task(sig):
	# Creates all tasks and puts them in queue. get() makes this function wait untill all tasks are completed
	# All output from the tasks are going to be appended in our results variable (it is a long list)
	results = group(benchmark.s(problem_to_solve,sig) for problem_to_solve in problems)().get()
    
	# Create bar chart with pygal
	line_chart = pygal.Bar()
	x_label_string = []
	time_list = []
	relerr_list = []
    
	for i in results:
		for key, value in i.iteritems():
			x_label_string.add(key)
			time_list.add(value[0])
			relerr_list.add(value[1])
          
	line_chart.x_labels = map(x_label_string)
	line_chart.add('Time', time_list)
	line_chart.add('Relative Error',  relerr_list)
	line_chart.y_title = "Relative usage of pronomen in tweets [%]"
	line_chart.title = "Usage of different pronumens in tweets"
	#line_chart.render()
	line_chart_data = line_chart.render_data_uri()
	
	return render_template("graphing.html", line_chart_data = line_chart_data)

if(__name__ == '__main__'):
	app.run(host = '0.0.0.0', debug = True)
