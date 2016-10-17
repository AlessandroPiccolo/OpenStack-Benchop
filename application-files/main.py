#curl -i http://127.0.0.1:5000/benchmark/api/v0.1/tasks
from flask import Flask, jsonify
#import oct2py
from oct2py import octave
from celery_tasks import make_celery
import time

app = Flask(__name__)


app = Flask(__name__)
app.config['CELERY_BROKER_URL']='amqp://guest@localhost//'
app.config['CELERY_BACKEND']='amqp://'

problems = ['prob1.m','prob2.m','prob3.m']
#allResults = {}
allResults = []


celery = make_celery(app)
@app.route('/benchmark',methods=['GET'])
def get_tasks():
    #return jsonify(results1,results2)  #will return the json
    start_time = time.time()
    for data in problems:
      #print data
      results = benchmark(data)
      #allResults.update(("The times:\n %s, \n\n The relative errors:\n %s \n" % (results)))
      #allResults[data] = results
      allResults.append(results)
      #allResults[data] = ("The times:\n %s, \n\n The relative errors:\n %s \n" % (results))
      print data + " \nThe times:\n %s, \n\n The relative errors:\n %s \n" % (results)

    print("---Execution time %s seconds ---" % (time.time() - start_time))
    return str(allResults)
    
@app.route('/benchmarkAll',methods=['GET'])
def get_tasks1():
    #return jsonify(results1,results2)  #will return the json
      start_time = time.time()
      results = benchmark(problems[0]) + benchmark1(problems[1]) + benchmark2(problems[2]) 
      print("---Execution time %s seconds ---" % (time.time() - start_time))
      #allResults.update(("The times:\n %s, \n\n The relative errors:\n %s \n" % (results)))
      #allResults[data] = results
      #allResults.append(results)
      #allResults[data] = ("The times:\n %s, \n\n The relative errors:\n %s \n" % (results))
      #print " \nThe times:\n %s, \n\n The relative errors:\n %s \n" % (results)
      print " Results from BanchAll", (results)
      return str(results)


@celery.task(name='main.benchmark')
def benchmark(problemName):
        octave.run(problemName)

	return octave.timeBSeuCallUI(), octave.relerrBSeuCallUI()

@celery.task(name='main.benchmark1')
def benchmark1(problemName):
        octave.run(problemName)

	return octave.timeBSeuCallUI(), octave.relerrBSeuCallUI()


@celery.task(name='main.benchmark2')
def benchmark2(problemName):
        octave.run(problemName)

	return octave.timeBSeuCallUI(), octave.relerrBSeuCallUI()

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug = True)
