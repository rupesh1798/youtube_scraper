from datetime import datetime, timedelta

from pymodm import MongoModel, fields
from pymongo import DESCENDING, IndexModel
from videos.managers import VideoManager


class Video(MongoModel):
    '''Model to maintain videos.

    Attributes:
        createdOn: Datetime object
        updatedOn: Datetime object
        title
        description
        publishedAt
        thumbnailURL
        channelTitle
        videoURL
    '''

    createdOn = fields.DateTimeField(required=False, default=lambda: datetime.now())
    updatedOn = fields.DateTimeField(required=False, default=lambda: datetime.now())
    title = fields.CharField(required=True)
    description = fields.CharField(blank=True)
    publishedAt = fields.DateTimeField(required=False, default=lambda: datetime.now())
    thumbnailURL = fields.URLField(required=False)
    channelTitle = fields.CharField(required=True)
    videoURL = fields.URLField(required=False)
    objects = VideoManager()

    class Meta:
        collection_name = 'Videos'
        indexes = [
            IndexModel(
                [
                    ('publishedAt', DESCENDING),
                ],
                background=True
            )
        ]
        final = True
