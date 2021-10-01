
import pymongo
import json


'''
Artifact Classes
'''
# Super Class Artifact
# TODO: FINISH the artifact class
# TODO all the artifact classes have an anotation
# class: Artifact:
#     def __init__


class Keystroke:
    def __init__(self):
        self.test = 'test'

    def data_to_dict(self):
        return {'test' : self.test}


'''
Database Classes
'''

# Super Class
class Database:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        # Accessing the AVERT database
        self.database = self.client['AVERT']
    def data_to_json(self, data): # TODO: delete later
        return json.dumps(data)


# Sub Classes
class KeystrokeCollection(Database):
    def __init__(self):
        super().__init__()
        # Accessing the Keystroke collection
        self.collection = self.database.keystroke

    def create(self, keystroke):
        self.collection.insert_one(keystroke.data_to_dict())


    #TODO: implement the below
    # def read
    # def update
    # def deleteSS


# Testing
if __name__ == '__main__':
    keystroke_collection = KeystrokeCollection()
    keystroke1 = Keystroke()
    keystroke_collection.create(keystroke1)

    # showing the databases
    print(keystroke_collection.client.list_database_names())