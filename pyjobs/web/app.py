from flask import Flask, render_template, make_response
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
        "index.html",
    )


@app.route('/r')
def redir():
    return render_template(
        "redirect.html",
    )


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


class JobResource(Resource):

    def get(self):
        return mongo.db.jobs.find()

api.add_resource(JobResource, '/api/jobs')
