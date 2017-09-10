"""
Crawling
"""
import random
import re
import web_scraping_with_python.helper_func as helper_funcs

from datetime import datetime

url_target = "http://en.wikipedia.org/wiki/Kevin_Bacon"
seed = random.seed(datetime.utcnow())

parsed_page = helper_funcs.get_page(url_target)
if parsed_page:
    links = parsed_page.find('div', {'id': 'bodyContent'}).find_all('a', {'href': re.compile("^(/wiki/)((?!:).*$)")})
    counter = 0
    while len(links) > 0 and counter < 6:
        rand_index = random.randint(0, len(links) - 1)
        new_article = links[rand_index].attrs.get('href')
        url_target = "http://en.wikipedia.org" + new_article
        new_page = helper_funcs.get_page(url_target)
        if new_page:
            links = parsed_page.find('div', {'id': 'bodyContent'}).find_all('a', {'href': re.compile("^(/wiki/)((?!:).*$)")})
            print(new_page.title.get_text())
        counter += 1