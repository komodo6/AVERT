from app import db


class VideoDAO:
    def __init__(self) -> None:
        self.db = db.Videos

    def create(self, video):
        if video is not None:
            self.db.insert(video.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read_id(self, video_id=None):
        # print(self.db.find({}))
        return self.db.find({"id": video_id}, {'_id': False})

    def read_all(self):
        return self.db.find({}, {'_id': False})

    def read_time_interval(self, end_range):
        print('end_range in read interval',end_range.strftime("%Y-%m-%d %H:%M:%S.%f")) #TODO: Delete 
        range = {
            "timestamp":{
                "$lt": end_range.strftime("%Y-%m-%d %H:%M:%S.%f")   
            }
        }
        video_list = []
        v = self.db.find(range)
        for doc in v:
            video_list = video_list + [doc]
        return video_list

    def update(self, video):
        if video is not None:
            self.db.save(video.toJSON())
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

    def delete(self, video):
        if video is not None:
            self.db.remove({'id': video})
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")

    def get_count(self):
        print(self.db.count())
        return self.db.count()
