import eel
from scraper import InstagramScraper

insta_scraper = InstagramScraper() 

eel.init('web')

# @eel.expose
# def send_data(msg):
#     print(msg)

@eel.expose
def scrape(query, amount):
    insta_scraper.scrape(query, amount)

eel.start("index.html", size=(400, 400))