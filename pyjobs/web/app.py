from flask import Flask, render_template
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Api, Resource

from bson.json_util import dumps

app = Flask(__name__)

# register extensions
app.config['MONGO_DBNAME'] = 'pyjobs'
mongo = PyMongo(app)
api = Api(app)


@app.route('/')
def hello():
    return render_template(
        "home.html",
        jobs=mongo.db.jobs.find()
    )


class JobResource(Resource):

    def get(self):
        return {
            'status': 'OK',
            'jobs': dumps(mongo.db.jobs.find())
        }

api.add_resource(JobResource, '/api/jobs')
