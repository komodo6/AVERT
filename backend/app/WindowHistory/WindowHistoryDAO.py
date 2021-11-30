from app import db

class WindowHistoryDAO:
    def __init__(self) -> None:
        self.db = db.WindowHistories

    def create(self, wh):
        if wh is not None:
            self.db.insert(wh.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read(self, wh_id=None):
        # print(self.db.find({}))
        if wh_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": wh_id}, {'_id': False})

    def read_time_interval(self, end_range):
        print('end_range in read interval',end_range.strftime("%Y-%m-%d %H:%M:%S.%f")) #TODO: Delete 
        range = {
            "timestamp":{
                "$lt": end_range.strftime("%Y-%m-%d %H:%M:%S.%f")   
            }
        }
        windowhistory_list = []
        wh = self.db.find(range)
        for doc in wh:
            windowhistory_list = windowhistory_list + [doc]
        return windowhistory_list

    def update(self, wh):
        if wh is not None:
            self.db.save(wh.toJSON())
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

    def delete(self, wh):
        if wh is not None:
            self.db.remove(wh.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")

    def get_count(self):
        print(self.db.count())
        return self.db.count()        
