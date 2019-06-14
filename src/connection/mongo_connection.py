import os

from pymongo import MongoClient

class MongoConnection():
    connection = None

    def __init__(self, static = True):
        self.static = static
        self.connect()

    def connect(self):
        if self.static:
            self.connection = MongoClient(self._getStaticConnection())
        else:
            print('Unauthorized connection')

        self.database = self.connection.get_default_database()

    def _getStaticConnection(self):
        # server = os.environ.get('MONGODB_SERVER')
        # port = os.environ.get('MONGODB_PORT')
        # user = os.environ.get('MONGODB_USER')
        # password = os.environ.get('MONGODB_PASSWORD')
        # database = os.environ.get('MONGODB_DATABASE')

        server = 'ds231207.mlab.com'
        port = 31207
        user = 'sympla'
        password = 'Sympla%402019'
        database = 'sympla'

        return 'mongodb://{}:{}@{}:{}/{}'.format(user, password, server, port, database)
