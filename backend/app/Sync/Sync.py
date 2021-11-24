from app import db
from pymongo import MongoClient

class Sync():
    def __init__(self, ip, collections) -> None:
        self.ip = ip
        self.collections = collections

    def start_sync(self):
        try:
            client = MongoClient(host=self.ip, port=27017)
            for c in self.collections:
                client[c].insert_many(db[c].find())
            return('Synced')
        except Exception as e:
            print(e)
            return('Error')