import os
import datetime
from celery import shared_task
from googleapiclient.discovery import build

from videos.models import Video


@shared_task()
def fetch_videos(autoretry_for=(Exception,), retry_kwargs={'max_retries': 3}):
    '''
    Job to fetch videos details

    '''

    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    api_service_name = "youtube"
    api_version = "v3"
    date = datetime.datetime.now() - datetime.timedelta(minutes=10)

    threshold_date = date.strftime("%Y-%m-%dT%H:%M:%SZ")
    result_type = "video"
    part = "snippet"
    max_results = 100
    query = os.environ.get("QUERY")

    keys_list = [key for key in os.environ.get("API_KEYS").split(",")]

    youtube = build(api_service_name, api_version, developerKey=keys_list[0])

    request = youtube.search().list(
        part=part,
        maxResults=max_results,
        publishedAfter=threshold_date,
        q=query,
        type="video"
    )

    response = request.execute()

    videos = [{
        "createdOn": datetime.datetime.now(),
        "updatedOn": datetime.datetime.now(),
        "title": video["snippet"].get("title"),
        "description": video["snippet"].get("description"),
        "thumbnailURL": video["snippet"].get("thumbnails", {}).get("default", {}).get("url"),
        "publishedAt": video["snippet"].get("publishedAt"),
        "channelTitle": video["snippet"].get("channelTitle"),
        "videoURL": f'https://www.youtube.com/watch?v={video["id"].get("videoId")}',
      } for video in response["items"]]

    video_details = sorted(videos, key=lambda obj: obj.get('publishedAt', '0'), reverse=True)
    Video.objects.remove({})
    Video.objects.insert_documents(video_details)
