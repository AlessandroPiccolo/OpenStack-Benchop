#curl -i http://127.0.0.1:5000/benchmark/api/v0.1/tasks


from celery_tasks import benchmark
from flask import Flask,jsonify
from oct2py import octave

app = Flask(__name__)

#problem = ('problem.m')
#solver1 =  ('solver1.m')
#solver2 =  ('solver2.m')
#results1 = benchmark(problem,solver1)
#results1 = benchmark(problem,solver2)

#get the results via celery worker
#results = benchmark()
#results = octave.run('Table.m')

@app.route('/benchmark/api/v0.1/tasks',methods=['GET'])
def get_tasks():
    #return jsonify(results1,results2)  #will return the json
    results = benchmark()
    print 'The times'
    print results.timeBSeuCallUI()

    print 'The relative errors'
    print results.relerrBSeuCallUI()


if(__name__ == '__main__'):
    app.run(debug = True)
