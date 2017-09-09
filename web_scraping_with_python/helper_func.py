import requests

def get_url(target_url):
    try:
        page_request = requests.get(target_url)
        return page_request
    except requests.exceptions.RequestException as e:
        print(e, target_url)
        return False