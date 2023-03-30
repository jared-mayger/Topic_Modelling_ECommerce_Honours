import eel
from scraper import InstagramScraper

insta_scraper = InstagramScraper() 

@eel.expose
def scrape(query, amount):
    insta_scraper.scrape(query, amount)

