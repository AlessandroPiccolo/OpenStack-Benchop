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
from pygal.style import Style

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
problems = [1,3] # List, for python 3.x: list(range(1, 7))

# Enables user to ping flask to send an request to the rabbit queue
# We get x number of tasks depending on the number of problems definied
# in list variable "problem"
@app.route('/benchmark/<float:sig>',defaults={'sig': 0.15}, methods = ['GET'])
def start_benchmark_task(sig):
	# Creates all tasks and puts them in queue. get() makes this function wait untill all tasks are completed
	# All output from the tasks are going to be appended in our results variable (it is a long list)
	results = group(benchmark.s(problem_to_solve,sig) for problem_to_solve in problems)().get()
    
	# Create bar chart with pygal
	x_label_string = []
	time_list = []
	relerr_list = []
    
	for i in results:
		for key, value in i.iteritems():
			x_label_string.append(key)
			time_list.append(value[0])
			relerr_list.append(value[1])
		
		
	style_lightblue = Style(
        background='white',
        plot_background='rgba(0, 0, 255, 0.03)',
        foreground='rgba(0, 0, 0, 0.8)',
        foreground_light='rgba(0, 0, 0, 0.9)',
        foreground_dark='rgba(0, 0, 0, 0.7)',
        colors=('#F15854')
        )
	
	style_red = Style(
        background='white',
        plot_background='rgba(0, 0, 255, 0.03)',
        foreground='rgba(0, 0, 0, 0.8)',
        foreground_light='rgba(0, 0, 0, 0.9)',
        foreground_dark='rgba(0, 0, 0, 0.7)',
        colors=('#f94a39')
        )
	
	line_chart_time = pygal.Bar(style=style_lightblue)  
	line_chart_time.x_labels = map(str, x_label_string)
	line_chart_time.add('Time', time_list)
	line_chart_time.y_title = "Execution time [s]"
	line_chart_time.title = "Execution time for different option price solvers"
	#line_chart.render()
	line_chart_time_data = line_chart_time.render_data_uri()
	
	line_chart_rerr = pygal.Bar(style=style_red)  
	line_chart_rerr.x_labels = map(str, x_label_string)
	line_chart_rerr.add('Relative Error', relerr_list)
	line_chart_rerr.y_title = "Relative error"
	line_chart_rerr.title = "Relative error for different option price solvers"
	#line_chart.render()
	line_chart_rerr_data = line_chart_rerr.render_data_uri()
	
	return render_template("graphing.html", results = results, line_chart_time_data = line_chart_time_data, line_chart_rerr_data = line_chart_rerr_data)

if(__name__ == '__main__'):
	app.run(host = '0.0.0.0', debug = True)
