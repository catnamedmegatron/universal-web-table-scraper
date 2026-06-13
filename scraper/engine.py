import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import io

def fetch_and_parse(url):
    """Downloads the URL and extracts tables and the page title."""
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = rq.get(url, headers=head)

    if response.status_code != 200:
        return None, None, response.status_code

    soup = bs(response.content, 'html.parser')
    raw_title = soup.title.text.strip() if soup.title else "Webpage"
    safe_title = re.sub(r'[\\/*?:"<>|]', '', raw_title).replace(' ', '_')
    
    try:
        tables = pd.read_html(io.StringIO(response.text))
        return tables, safe_title, 200
    except ValueError:
        return [], safe_title, 200 # No tables found