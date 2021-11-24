from app import db
from pymongo import MongoClient

class Sync():
    def __init__(self, ip, collections) -> None:
        self.ip = ip
        self.collections = collections

    def start_sync(self):
        try:
            client = MongoClient(host=self.ip, port=27017)
            remote_db = client.AVERT
            for c in self.collections:
                if c in db.list_collection_names():
                    docs = db[c].find()
                    if docs is not None:
                        remote_db[c].insert_many(docs)
            return True
        except Exception as e:
            print(e)
            return False