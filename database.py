from pymongo import MongoClient

class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['Motorista']

    def get_collection(self, name):
        return self.db[name]