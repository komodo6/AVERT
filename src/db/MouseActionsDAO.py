from db import db


class MouseActionsDAO:
    def __init__(self) -> None:
        self.db = db.db.MouseActions

    def create(self, mouse_action):
        if mouse_action is not None:
            self.db.insert(mouse_action.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read(self, mouse_action_id=None):
        # print(self.db.find({}))
        if mouse_action_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": mouse_action_id}, {'_id': False})

    def update(self, mouse_action):
        if mouse_action is not None:
            self.db.save(mouse_action.toJSON())
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, mouse_action):
        if mouse_action is not None:
            self.db.remove(mouse_action.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")
