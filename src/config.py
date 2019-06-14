import logging
import os

DEBUG = os.getenv('ENVIRONEMENT') == 'DEV'
APPLICATION_ROOT = os.getenv('APPLICATION_APPLICATION_ROOT', '/application')
HOST = os.getenv('APPLICATION_HOST')
PORT = int(os.getenv('APPLICATION_PORT', '3000'))

DB_CONTAINER = os.getenv('APPLICATION_DB_CONTAINER', 'db')
MONGODB = {
    'user': os.getenv('APPLICATION_MONGO_USER', 'sympla'),
    'pw': os.getenv('APPLICATION_MONGO_PW', 'Sympla%402019'),
    'host': os.getenv('APPLICATION_MONGO_HOST', 'ds231207.mlab.com'),
    'port': os.getenv('APPLICATION_MONGO_PORT', 31207),
    'db': os.getenv('APPLICATION_MONGO_DB', 'sympla'),

    # 'user': os.getenv('APPLICATION_MONGO_USER', 'sympla'),
    # 'pw': os.getenv('APPLICATION_MONGO_PW', ''),
    # 'host': os.getenv('APPLICATION_MONGO_HOST', DB_CONTAINER),
    # 'port': os.getenv('APPLICATION_MONGO_PORT', 27017),
    # 'db': os.getenv('APPLICATION_MONGO_DB', 'postgres'),
}
# DB_URI = 'mongodb://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % MONGODB
DB_URI = 'mongodb://{}:{}@{}:{}/{}'.format(MONGODB['user'], MONGODB['pw'], MONGODB['host'], MONGODB['port'], MONGODB['db'])

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)
