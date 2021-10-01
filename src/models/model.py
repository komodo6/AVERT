
import pymongo
import json
'''
Artifact Classes
'''
# Super Class
class Artifact:
    _annotations = ""
    _time_created = ""
    def __init__(self):
        pass

# Sub Class
class Keystroke(Artifact):
    def __init__(self):
        super().__init__()
        self.test = 'test'

    def data_to_dict(self):
        return {'test' : self.test}

class MouseAction(Artifact):
    def __init__(self):
        super().__init__()
        self.test = 'test'

    def data_to_dict(self):
        return {'test' : self.test}


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

    def create(self, keystroke):
        self.collection.insert_one(keystroke.data_to_dict())

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

    # TODO: implement the below
    # def read
    # def update
    # def delete

# Testing
if __name__ == '__main__':
    keystroke_collection = KeystrokeCollection()
    keystroke1 = Keystroke()
    keystroke_collection.create(keystroke1)

    mouse_action_collection = MouseActionCollection()
    mouse_action1 = MouseAction()
    mouse_action_collection.create(mouse_action1)