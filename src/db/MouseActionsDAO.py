from db.db import db

class MouseActionsDAO:
    def __init__(self) -> None:
        self.db = db

    def create(self, mouse_action):
        if mouse_action is not None:
            self.db.MouseActions.insert(mouse_action.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")
    
    def read(self, mouse_action_id):
        if mouse_action_id is None:
            self.db.MouseActions.find({})
        else:
            return self.db.MouseActions.find({"id": mouse_action_id})

    #TODO: add read_all to read all the entries in the MouseActions

    def update(self, mouse_action):
        if mouse_action is not None:
            self.db.MouseActions.save(mouse_action.toJSON())
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, mouse_action):
        if mouse_action is not None:
            self.db.MouseActions.remove(mouse_action.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")
    


