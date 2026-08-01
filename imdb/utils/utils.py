import re
import sys
import time

import nltk
import pandas as pd
import unidecode

from bs4 import BeautifulSoup
from requests import get

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from textblob import TextBlob

# Chrome driver management is handled automatically by Selenium Manager
# (bundled with selenium>=4.6), so no separate chromedriver package is needed.

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

from nltk.sentiment import SentimentIntensityAnalyzer
