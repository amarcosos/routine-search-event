import sys

from connection.mongo_connection import MongoConnection

class DestinationRepository():
  def __init__(self):
    self.mongoConnection = MongoConnection()
    self.collection = self.mongoConnection.database.get_collection('events')

  def insertMany(self, data):
    for item in data:
      self.collection.update({ '_id': item.get('_id') }, item, True)
    # self.collection.update_many({ '_id': data['_id'] }, data, True)
    # self.collection.insert(data)
