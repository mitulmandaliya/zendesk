from flask import Flask, jsonify, Blueprint
from flask_restful import Api, Resource
from werkzeug.exceptions import HTTPException, default_exceptions
from app.views.tickets import Tickets, Ticket
from flasgger import Swagger


def json_app(flask_app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {
                'code': error.code,
                'message': error.description
            }
        else:
            result = {
                'code': 500,
                'message': "Something went wrong"
            }
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        flask_app.register_error_handler(code, error_handling)

    return flask_app

ZD_API_V1 = '/zd/api/%s'

application = json_app(Flask(__name__))

application.config['SWAGGER'] = {
    'title': 'ZD', 'specs_route': ZD_API_V1 % 'apidocs'}

Swagger(application)

zendesk_blueprint = Blueprint('zd-v1', __name__)

api = Api(zendesk_blueprint)

application.register_blueprint(zendesk_blueprint, url_prefix='/zd/api')



api.add_resource(Tickets, '/tickets')
api.add_resource(Ticket, '/tickets/<string:id>')


if __name__=="__main__":
    application.run(host='127.0.0.1', port=5001)