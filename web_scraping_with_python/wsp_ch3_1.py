"""
Crawling
"""
import helper_func

from bs4 import BeautifulSoup

url_target = "http://www.pythonscraping.com/pages/page3.html"

page_request = helper_func.get_url(url_target)
if page_request:
    parsed_page = BeautifulSoup(page_request.text, 'html.parser')