from app import db


class ScreemshotDAO:
    def __init__(self) -> None:
        self.db = db.Screenshots

    def create(self, screenshot):
        if screenshot is not None:
            self.db.insert(screenshot.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read_id(self, screen_shot_id=None):
        # print(self.db.find({}))
        return self.db.find({"id": screen_shot_id}, {'_id': False})

    def read_all(self):
        return self.db.find({}, {'_id': False})

    def read_time_interval(self, end_range):
        print('end_range in read interval',end_range.strftime("%Y-%m-%d %H:%M:%S.%f")) #TODO: Delete 
        range = {
            "timestamp":{
                "$lt": end_range.strftime("%Y-%m-%d %H:%M:%S.%f")   
            }
        }
        screenshot_list = []
        sc = self.db.find(range)
        for doc in sc:
            screenshot_list = screenshot_list + [doc]
        return screenshot_list

    def update(self, screenshot):
        if screenshot is not None:
            self.db.save(screenshot.toJSON())
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

    def delete(self, screenshot):
        if screenshot is not None:
            self.db.remove({'id': screenshot})
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")

    def get_count(self):
        print(self.db.count())
        return self.db.count()        
