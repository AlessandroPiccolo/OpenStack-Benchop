# Import the necessary package to process data in JSON format
from celery import Celery
from celery.result import AsyncResult

def make_celery(app):
	celery=Celery(app.import_name, backend=app.config['CELERY_BACKEND'],
		broker = app.config['CELERY_BROKER_URL'])
	celery.conf.update(app.config)
	TaskBase = celery.Task
	class ContextTask(TaskBase):
		abstract = True
		def __call__(self, *args, **kwargs):
			with app.app_context():
				return TaskBase.__call__(self,*args,**kwargs)
	celery.Task = ContextTask
	return celery

#octave.run('Table.m')




#create a celery application instance that connects to the default RabbitMQ service
#app = Celery('tasks', backend='amqp', broker='amqp://')


#def benchmark(problem,solver):
