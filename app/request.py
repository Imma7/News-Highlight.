from app import app
import urllib.request, json
from .models import news


#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_source_url = app.config['NEWS_SOURCE_API_BASE_URL']
base_article_url = app.config['NEWS_ARTICLES_API_BASE_URL']