from datetime import datetime, timedelta
from bson.objectid import ObjectId
from commons.utils.default_model_manager import DefaultManager
from pymongo import ReturnDocument


class VideoManager(DefaultManager):
    def insert_documents(self, video_details):
        '''Method to create search history object for a particular user for first time search.

        Args:
            user_id: Id of user.
            empi: empi of searched patient.
        '''

        self.model.objects.insert_many(video_details)

    def fetch_videos(self, doc_id, page_size):
        '''Method to fetch search history for a particular user.

        Args:
            user_id: Id of user.

        Response:
            doc: list of search history objects.
        '''

        if doc_id:
            pipeline = [
                {
                    '$match': {
                        '_id': {'$gt': ObjectId(doc_id)}
                    }
                },
                {
                    '$limit': int(page_size)
                }
            ]
        else:
            pipeline = [
                {
                    '$limit': int(page_size)
                }
            ]

        return list(self.model.objects.aggregate(*pipeline)) or []

    def search_videos(self, query):
        '''Method to create search history object for a particular user for first time search.

        Args:
            user_id: Id of user.
            empi: empi of searched patient.
        '''

        return self.model.objects.get_all(queries=query)
