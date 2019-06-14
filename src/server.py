from flask import Flask
from flask.blueprints import Blueprint
from flasgger import Swagger

import config
# from models import db
# import routes

server = Flask(__name__)

server.config['SWAGGER'] = {
  'swagger_version': '2.0',
  'title': 'Application',
  'specs': [
    {
      'version': '0.0.1',
      'title': 'Application',
      'endpoint': 'spec',
      'route': '/application/spec',
      'rule_filter': lambda rule: True  # all in
    }
  ],
  'static_url_path': '/application/apidocs'
}

Swagger(server)

server.debug = config.DEBUG
server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
# db.init_app(server)
# db.app = server

# for blueprint in vars(routes).values():
#   if isinstance(blueprint, Blueprint):
#     server.register_blueprint(
#       blueprint,
#       url_prefix=config.APPLICATION_ROOT
#     )

if __name__ == '__main__':
  server.run(host=config.HOST, port=config.PORT)
