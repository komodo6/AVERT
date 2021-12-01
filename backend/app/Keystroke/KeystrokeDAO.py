from app import db


class KeystrokeDAO:
    def __init__(self) -> None:
        self.db = db.Keystrokes

    def create(self, keystroke):
        if keystroke is not None:
            self.db.insert(keystroke.toJSON())
        else:
            raise Exception("Cannot Insert, Keystroke is empty")

    def read(self, keystroke_id=None):
        if keystroke_id is None:
            print(self.db)
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": keystroke_id}, {'_id': False})

    def read_time_interval(self, end_range):
        print('end_range in read interval',end_range.strftime("%Y-%m-%d %H:%M:%S.%f")) #TODO: Delete 
        range = {
            "timestamp":{
                "$lt": end_range.strftime("%Y-%m-%d %H:%M:%S.%f")   
            }
        }
        ks_list = []
        ks = self.db.find(range)
        for doc in ks:
            ks_list = ks_list + [doc]
        return ks_list

    def get_count(self):
        print(self.db.count())
        return self.db.count()

    def update(self, keystroke):
        if keystroke is not None:
            self.db.save(keystroke.toJSON())
        else:
            raise Exception("Cannot update, keystroke is empty")

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

    def delete(self, keystroke):
        if keystroke is not None:
            self.db.remove(keystroke.toJSON())
        else:
            raise Exception("Cannot Delete, Keystroke is empty")
