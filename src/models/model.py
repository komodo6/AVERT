
import pymongo
import json
'''
Artifact Classes
'''
# Super Class
class Artifact:
    _time_created = ""
    _date_created = ""
    _ip = ""
    _mac = ""
    _annotations = ""
    def __init__(self, time_created, date_created, ip, mac, annotations):
        self._time_created = time_created
        self._date_created = date_created
        self._ip = ip
        self._mac = mac
        self._annotations = annotations

    def data_to_dict(self):
        return {
            'time_created' : self._time_created,
            'date_created' : self._date_created,
            'ip': self._ip,
            'mac': self._mac,
            'annotations' : self._annotations
        }

# Sub Class
class Keystroke(Artifact):
    _value = ""
    def __init__(self,time_created, date_created, ip, mac, annotations, value):
        super().__init__(time_created, date_created, ip, mac, annotations)
        self._value = value

    def data_to_dict(self):
        return {**super().data_to_dict(), 'value':self._value}

class MouseAction(Artifact):
    _type = ""
    _coordinate = ""
    def __init__(self,time_created, date_created, ip, mac, annotations, type, coordinate):
        super().__init__(time_created, date_created, ip, mac, annotations)
        self._type = type
        self._coordinate = coordinate

    def data_to_dict(self):
        return {**super().data_to_dict(), 'type':self._type, 'coordinate':self._coordinate}



'''
Database Classes
'''

# Super Class
class DatabaseCollection:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
        # Accessing the AVERT database
        self.database = self.client['AVERT']

# Sub Classes
class KeystrokeCollection(DatabaseCollection):
    def __init__(self):
        super().__init__()
        # Accessing the Keystroke collection
        self.collection = self.database.keystrokes

    def create(self, keystroke_data):
        self.collection.insert_one(keystroke_data)

    def read_all(self):
        cursor = self.collection.find({})
        docs = []
        for doc in cursor:
            docs = docs + [doc]
        return docs

    #TODO: implement the below
    # def read
    # def update
    # def delete

class MouseActionCollection(DatabaseCollection):
    def __init__(self):
        super().__init__()
        # Accessing the Mouse Action collection
        self.collection = self.database.mouse_actions

    def create(self, mouse_action):
        self.collection.insert_one(mouse_action.data_to_dict())

    def read_all(self):
        cursor = self.collection.find({})
        docs = []
        for doc in cursor:
            docs = docs + [doc]
        return docs

    # TODO: implement the below
    # def read
    # def update
    # def delete

# Testing
if __name__ == '__main__':
    keystroke_collection = KeystrokeCollection()
    keystroke1 = Keystroke('00:00:11 UTC','03/19/2021','192.192.192.192',"66-37-BD-34-32-D1","this is important","ENTER")
    keystroke_collection.create(keystroke1.data_to_dict())
    print(keystroke_collection.read_all())

    mouse_action_collection = MouseActionCollection()
    mouse_action1 = MouseAction('00:00:11 UTC','03/19/2021','192.192.192.192',"66-37-BD-34-32-D1","this is important","Right Click", "X: 10 Y: 11")
    mouse_action_collection.create(mouse_action1)
    print(mouse_action_collection.read_all())