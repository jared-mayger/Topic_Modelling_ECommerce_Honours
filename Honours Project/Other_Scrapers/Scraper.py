from instagrapi import Client
import pandas as pd
from urllib.parse import urlparse
import requests
import re
import eel 

from instagrapi.exceptions import (
    PhotoConfigureError,
    PhotoConfigureStoryError,
    PhotoNotUpload,
)

def scrape(query, amount): 
    client = Client()
    query = input("Please enter the Hashtag you want to scrape: ")
    #amount = input("Please enter the amount of posts you want to scrape: ")

    #query = query
    #amount = int(amount)
    ACCOUNT_USERNAME = 'jmayger_instagrapi'
    ACCOUNT_PASSWORD = 'INSTAGRAPI'
    client.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

    posts = client.hashtag_medias_recent_v1(query, amount)

    df= pd.DataFrame(posts)
    posts_df = pd.DataFrame(posts, columns=['pk', 'id', 'code', 'taken_at', 'media_type', 'product_type', 'Thumbnail_url', 'Location', 'User', 'comment_count', 'like_count', 'has_liked', 'caption_text', 'accessibility_caption', 'usertags', 'video_url', 'view_count', 'video_duration', 'title', 'resources', 'clips_metadata'])
    posts_json = posts_df.to_json('./posts.json', orient='index')

    index = 0
    for p in posts:
        if p.thumbnail_url != None:
            client.photo_download_by_url(p.thumbnail_url, "Image " + str(index), folder="./images")
        index += 1

