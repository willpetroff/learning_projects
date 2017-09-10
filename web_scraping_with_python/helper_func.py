import requests

from bs4 import BeautifulSoup


def get_url(target_url):
    try:
        page_request = requests.get(target_url)
        return page_request
    except requests.exceptions.RequestException as e:
        print(e, target_url)
        return False


def get_page(target_url, parser='html.parser'):
    target_page = get_url(target_url)
    if target_page:
        parsed_page = BeautifulSoup(target_page.text, parser)
        return parsed_page
    return None