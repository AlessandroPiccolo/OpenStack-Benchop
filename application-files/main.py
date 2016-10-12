#curl -i http://127.0.0.1:5000/benchmark/api/v0.1/tasks
from flask import Flask
#import oct2py
from oct2py import octave
from celery_tasks import make_celery


app = Flask(__name__)
#problem = ('problem.m')
#solver1 =  ('solver1.m')
#solver2 =  ('solver2.m')
#results1 = benchmark(problem,solver1)
#results1 = benchmark(problem,solver2)

#get the results via celery worker
#results = benchmark()
#results = octave.run('Table.m')
app = Flask(__name__)
app.config['CELERY_BROKER_URL']='amqp://guest@localhost//'
app.config['CELERY_BACKEND']='amqp://'

celery = make_celery(app)
@app.route('/benchmark',methods=['GET'])
def get_tasks():
    #return jsonify(results1,results2)  #will return the json
    results = benchmark()
    #print 'The times'
    octave.run('Table.m')
    #print results.timeBSeuCallUI()
    #print 'The relative errors'
    #print results.relerrBSeuCallU	I()
    return(("The times: %s, The relative errors: %s" % (octave.timeBSeuCallUI,octave.relerrBSeuCallUI)))
    #create a celery application instance that connects to the default RabbitMQ service
#def benchmark(problem,solver)
@celery.task(name='main.benchmark')
def benchmark():
#	oc = oct2py.Oct2Py()
#	result = oc.run('Table.m')
	octave.run('Table.m')
	#res = octave.who()
	print octave.timeBSeuCallUI()
	print octave.relerrBSeuCallUI()
#	return results

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug = True)
