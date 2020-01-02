import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import config

application = Flask(__name__)

#application.config["MONGO_URI"] = os,environ['MONGODB_USERNAME']
#application.config["MONGO_URI"] = config.MONGO_DB_URL
#application.config["MONGO_URI"] = os.environ['MONGODB_URI_PREFIX'] + 
#									os.environ['MONGODB_USERNAME'] + ':' + 
#									os.environ['MONGODB_PASSWORD'] + '@' +
#									os.environ['MONGODB_HOSTNAME'] + ':27017/' + 
#									os.environ['MONGODB_DATABASE']

application.config["MONGO_URI"] = os.environ['MONGODB_URI_PREFIX'] + 
									os.environ['MONGODB_USER'] + ':' + 
									os.environ['MONGODB_PWD'] + '@' + 
									os.environ['MONGODB_DB'] + 
									os.environ['MONGODB_URI_SUFFIX'] +
									os.environ['MONGODB_URI_EXTRA_PYTHON_SUFFIX']
#mongodb+srv://to:<password>@airportdata-lhzto.mongodb.net/test?retryWrites=true&w=majority

mongo = PyMongo(application)
db = mongo.db

@application.route('/')
def index():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )

#@application.route('/todo')
#def todo():
#    _todos = db.todo.find()
#
#    item = {}
#    data = []
#    for todo in _todos:
#        item = {
#            'id': str(todo['_id']),
#            'todo': todo['todo']
#        }
#        data.append(item)
#
#    return jsonify(
#        status=True,
#        data=data
#    )

@app.route(config.SERVER_WORKDIR, methods=['POST'])
def get_airport_details_by_city_name():
	col = db.airport_collection

	# res = col.find({'City': {'$regex': '/vic/i'}})
	res = col.find({"City": {
                "$regex": "ha",
                "$options": 'i'
                }
                }
                )

	
	#list_of_dict = list(res)

	return jasonify(list(res))
        
	
#@application.route('/todo', methods=['POST'])
#def createTodo():
#    data = request.get_json(force=True)
#    item = {
#        'todo': data['todo']
#    }
#    db.todo.insert_one(item)
#
#    return jsonify(
#        status=True,
#        message='To-do saved successfully!'
#    ), 201

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
