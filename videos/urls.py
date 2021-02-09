from django.urls import include, path
from videos.views import manage_videos, manage_videos_search

app_name = 'videos'


urlpatterns = [
    path('videos', manage_videos, name='manage_videos'),
    path('videos/search', manage_videos_search, name='manage_videos_search')
]
