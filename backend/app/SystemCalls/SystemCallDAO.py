from app import db


class SystemCallDAO:
    def __init__(self) -> None:
        self.db = db.SystemCall

    def create(self, systemcall):
        if systemcall is not None:
            self.db.insert(systemcall.toDict())
        else:
            raise Exception("Cannot Insert, System Call is empty")

    def read(self, process_id=None):
        # print(self.db.find({}))
        if process_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": process_id}, {'_id': False})

    def update(self, process):
        if process is not None:
            self.db.save(process.toJSON())
        else:
            raise Exception("Cannot update, System Call is empty")

    def update_tag(self, id, tags):
        if id is not None:
            self.db.update({'id': id}, {
                "$set": {
                    'tags': tags
                }
            }, upsert=False, multi=False)
        else:
            raise Exception("Cannot update, System Call is empty")

    def delete(self, process):
        if process is not None:
            self.db.remove(process.toJSON())
        else:
            raise Exception("Cannot Delete, System Call is empty")

    def get_count(self):
        print(self.db.count())
        return self.db.count()        
