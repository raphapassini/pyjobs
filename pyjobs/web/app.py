from flask import Flask, render_template, make_response, request
from flask.ext.pymongo import PyMongo
from flask.ext.restful import Api, Resource
from bson.json_util import dumps
from bson import Code
from mongo_filter import where_from_request

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
        where = where_from_request(request)
        return mongo.db.jobs.find(where)


class CityResource(Resource):

    def get(self):
        map_func = Code(
            "function() { "
            "if(this.city.trim() != '')"
            "emit(this.city.toUpperCase().trim(), 1) }"
        )
        reduce_func = Code(
            "function(key, values) { return values.length }"
        )
        result = mongo.db.jobs.map_reduce(map_func, reduce_func, "myresults")
        return result.find()


api.add_resource(JobResource, '/api/jobs')
api.add_resource(CityResource, '/api/cities')
