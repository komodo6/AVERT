from app import db


class MouseActionsDAO:
    def __init__(self) -> None:
        self.db = db.MouseActions

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

    def read_time_interval(self, end_range):
        print('end_range in read interval',end_range.strftime("%Y-%m-%d %H:%M:%S.%f")) #TODO: Delete 
        range = {
            "timestamp":{
                "$lt": end_range.strftime("%Y-%m-%d %H:%M:%S.%f")   
            }
        }
        mouseactions_list = []
        ma = self.db.find(range)
        for doc in ma:
            mouseactions_list = mouseactions_list + [doc]
        return mouseactions_list


    def update(self, mouse_action):
        if mouse_action is not None:
            self.db.save(mouse_action.toJSON())
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def update_tag(self, id, tags):
        if id is not None:
            self.db.update({'id': id}, {
                "$set": {
                    'tags': tags
                }
            }, upsert=False, multi=False)
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def update_annotation(self, id, annotation):
        if id is not None:
            self.db.update({'id': id}, {
                "$set": {
                    'annotations': annotation
                }
            }, upsert=False, multi=False)
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, mouse_action):
        if mouse_action is not None:
            self.db.remove(mouse_action.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")

    
    def get_count(self):
        print(self.db.count())
        return self.db.count()