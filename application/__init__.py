import requests, os
from flask import Flask, request, render_template, abort, redirect, jsonify, make_response
from flask.ext.restful import Api, Resource


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
api = Api(app)
TABLEAU_URL = app.config['TABLEAU_URL']
API_ROOT_PATH = '/tableau'


@app.route('/')
def index():
    return 'A simple proxy for Tableau Server REST API that implement with Python, Flask, Flask-RESTful and Rquests.'


class TableauAPI(Resource):
    def get(self, url):
        apiUrl = TABLEAU_URL + '/' + url
        resp   = requests.get(apiUrl, headers={'X-Tableau-Auth': request.headers['X-Tableau-Auth']})
        if resp.status_code == 200:
            response = make_response(resp.text)
            response.headers['content-type'] = 'application/xml'
            return response
        else:
            abort(resp.status_code)

    def post(self, url):
        apiUrl = TABLEAU_URL + '/' + url
        resp   = requests.post(apiUrl, data=request.data, headers=request.headers)
        if resp.status_code == 200:
            response = make_response(resp.text)
            response.headers['content-type'] = 'application/xml'
            return response
        elif resp.status_code == 204:
            return '', 204
        else:
            abort(resp.status_code)


class TicketAPI(Resource):
    def get(self):
        apiUrl   = TABLEAU_URL + '/trusted'
        headers  = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        username = request.headers.get('Username')
        resp     = requests.post(apiUrl, data={'username': username}, headers=headers)
        if resp.status_code == 200:
            if resp.text != '-1':
                return {
                    'ticket': resp.text
                }, 200
            else:
                abort(404)
        else:
            abort(404)


api.add_resource(TableauAPI, API_ROOT_PATH + '/<path:url>')
api.add_resource(TicketAPI, API_ROOT_PATH + '/ticket')
