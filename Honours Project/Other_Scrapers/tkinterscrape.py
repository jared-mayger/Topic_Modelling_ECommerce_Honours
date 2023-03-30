import tkinter as tk
from tkinter import simpledialog
from instagrapi import Client
import pandas as pd
from urllib.parse import urlparse
import requests
import re

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog box
USER_INP = simpledialog.askstring(title="Hashtag",
                                  prompt="What Hashtag would you like to scrape? ")

client = Client()
query = USER_INP

ACCOUNT_USERNAME = 'jmayger_instagrapi'
ACCOUNT_PASSWORD = 'INSTAGRAPI'
client.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

posts = client.hashtag_medias_recent_v1(query, amount=20)
    #print("Scraping Instagram...")

df= pd.DataFrame(posts)
posts_df = pd.DataFrame(posts, columns=['pk', 'id', 'code', 'taken_at', 'media_type', 'product_type', 'Thumbnail_url', 'Location', 'User', 'comment_count', 'like_count', 'has_liked', 'caption_text', 'accessibility_caption', 'usertags', 'video_url', 'view_count', 'video_duration', 'title', 'resources', 'clips_metadata'])
posts_json = posts_df.to_json('./posts.json', orient='index')

index = 0
for p in posts:
    if p.thumbnail_url != None:
        client.photo_download_by_url(p.thumbnail_url, "Image " + str(index), folder="./images")
    index += 1