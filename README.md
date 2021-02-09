# youtube_scraper

API has be created to Stream, Search, filter Videos by a youtube streaming API

### Built With

1. Python3
2. Django 2.1
3. MongoDb
4. Celery
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* [Virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) - Setting up virtual environment
* [Pip](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) - Installing Pip
* [Homebrew](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/) - Installing Homebrew
* [Python3](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/)
* MongoDb
* Celery
* Redis

### Setup project (Installation Instructions)
**Change the Api credentials in .env file.**
* API_KEYS

Install the dependencies and devDependencies and start the server.

```sh
$ cd youtube_scraper
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

run celery in another terminal tab
### 1. API1 to fetch videos
API 1 = `http://127.0.0.1:8000/youtube/videos`

(methods supported - GET)

```
  {
    "metadata": {
        "count": 2,
        "nextUrl": "/youtube/videos?limit=10&reference_id=602237bf15157a3de00a5d70"
    },
    "data": [
        {
            "_id": "602237bf15157a3de00a5d6f",
            "createdOn": 1612855231000,
            "updatedOn": 1612855231000,
            "title": "watch cricket match Free. IND vs ENG | Thop TV App | shaheenTech13",
            "description": "friends. watch all the games and Cricket Free in Thop App. pehle aapko ye update krni pad skti hai. aap update krlena. agar app me technical error show hota ...",
            "publishedAt": 1612855140000,
            "thumbnailURL": "https://i.ytimg.com/vi/R_fII53feIc/default.jpg",
            "channelTitle": "ShaheenTech13",
            "videoURL": "https://www.youtube.com/watch?v=R_fII53feIc"
        },
        {
            "_id": "602237bf15157a3de00a5d70",
            "createdOn": 1612855231000,
            "updatedOn": 1612855231000,
            "title": "real cricket best catch of the decade",
            "description": "",
            "publishedAt": 1612855140000,
            "thumbnailURL": "https://i.ytimg.com/vi/Yt6epXHz2YQ/default.jpg",
            "channelTitle": "Heshe Elwhat",
            "videoURL": "https://www.youtube.com/watch?v=Yt6epXHz2YQ"
        }
    ]
}
 ```
By default there are 10 entries in every page.
**Default time for streaming is 10 minutes. you can change the Stream time in tasks.py and settings.py file**

### 2. API2 to youtube/search
This API fetches the data stored based on the search keywords provided as required.
URL : `http://127.0.0.1:8000/youtube/videos/search`
Mehtod: POST
Body : {"videoURL": "https://www.youtube.com/watch?v=R_fII53feIc"}
#### Response
Response by the API in Raw form

```
{
    "metadata": {
        "count": 1
    },
    "data": [
        {
            "_id": "602237bf15157a3de00a5d6f",
            "createdOn": 1612855231000,
            "updatedOn": 1612855231000,
            "title": "watch cricket match Free. IND vs ENG | Thop TV App | shaheenTech13",
            "description": "friends. watch all the games and Cricket Free in Thop App. pehle aapko ye update krni pad skti hai. aap update krlena. agar app me technical error show hota ...",
            "publishedAt": 1612855140000,
            "thumbnailURL": "https://i.ytimg.com/vi/R_fII53feIc/default.jpg",
            "channelTitle": "ShaheenTech13",
            "videoURL": "https://www.youtube.com/watch?v=R_fII53feIc"
        }
    ]
}
```