"""
Downloader media Youtube
:url https://youtu.be/WVlkk2rXn2Y?si=U9Ee1lDVfKRHPqA9
"""

import os

import requests
from dotenv import load_dotenv

from src.http_exception import HttpException

load_dotenv()


def get_url_download(link_video: str):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    link_video = link_video.split("?")[0].split("/")[3]
    querystring = {
        "videoId": link_video,
        "urlAccess": "normal",
        "videos": "auto",
        "audios": "auto",
    }

    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": "youtube-media-downloader.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        raise HttpException(
            "Error fetching video details",
            response.status_code,
            response.json(),
        )
    print(response.json())
    return response.json()["audios"]["items"][0]["url"]


def download(link_video: str, filename: str = "audio.mp3"):
    url_download = get_url_download(link_video)
    content = requests.get(url_download)
    with open(filename, "wb") as f:
        f.write(content.content)
