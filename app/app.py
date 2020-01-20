import os

import pymongo
from flask import Flask, request, jsonify
from bson.json_util import dumps

# #  The following can be UNcommented for dev testing on local host (NOT in a Docker container)
# from dotenv import load_dotenv
# from pathlib import Path  # python3 only
# env_path = Path('..') / '.env'
# load_dotenv(dotenv_path=env_path)

# CLIENT ACCESS
# For Dockerized container
# curl -H "Content-type: application/json" -X GET http://0.0.0.0/city_search -d '{"City":"ter"}'
#  or
# curl -H "Content-type: application/json" -X GET http://127.0.0.1/city_search -d '{"City":"ter"}'
#
# N.B. As for testing on local host, add port number :8000 to URL

application = Flask(__name__)

client = pymongo.MongoClient(os.environ['MONGODB_URI_PREFIX']
                             + os.environ['MONGODB_USER'] + ':'
                             + os.environ['MONGODB_PWD'] + '@'
                             + os.environ['MONGODB_CLUSTER']
                             + os.environ['MONGODB_URI_SUFFIX']
                             + os.environ['MONGODB_URI_EXTRA_PYTHON_SUFFIX'])


@application.route('/')
def home():
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask app!'
    )


@application.route(os.environ['FLASK_SEARCH'], methods=['GET'])
def city_search():
    db = client[os.environ['MONGODB_DB']]
    collection = db[os.environ['MONGODB_COLLECTION']]

    city_name = request.json

    # Use regex with -i (ignore case)
    res = collection.find({"City": {
        "$regex": city_name['City'],
        "$options": 'i'
    }
    }
    )

    # None of the followings works: "not JSON serializable"
    # return json.dumps(res)
    # return bsonjs.dumps(res)
    # return jsonify(bsonjs.dumps(res))
    # return jsonify(results=list(res))
    return dumps(res)


if __name__ == "__main__":
    ENVIRONMENT_IP_ADDRESS = os.environ.get("FLASK_DEFAULT_IP_ADDRESS", "0.0.0.0")
    ENVIRONMENT_DEBUG = os.environ.get("FLASK_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("FLASK_PORT", 8000)
    application.run(host=ENVIRONMENT_IP_ADDRESS, port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
