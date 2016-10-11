## the idea based on the toturial https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

from celery import Celery
from oct2py import octave


#octave.run('Table.m')




#create a celery application instance that connects to the default RabbitMQ service
app = Celery('tasks', backend='amqp', broker='amqp://')


#def benchmark(problem,solver):

@app.task
def benchmark():

	return octave.run('Table.m')
        
