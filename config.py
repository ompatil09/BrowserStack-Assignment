import os
from dotenv import load_dotenv

load_dotenv()

# Base URLs
BASE_URL = "https://elpais.com"
OPINION_URL = "https://elpais.com/opinion/"

# Scraping config
ARTICLE_LIMIT = 5
IMAGES_DIR = "images"

# Translation API
Google_Translate_API = os.getenv("Google_Translate_API")
Google_Translate_HOST = "google-translate113.p.rapidapi.com"
Google_Translate_URL = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

# BrowserStack credentials (set these in .env)
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

# Parallel threads
PARALLEL_THREADS = 5