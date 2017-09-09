"""
Beautiful Soup: Selecting tags with find_all
"""
import helper_func

from bs4 import BeautifulSoup

url_target = "http://www.pythonscraping.com/pages/warandpeace.html"

page_request = helper_func.get_url(url_target)
if page_request:
    parsed_page = BeautifulSoup(page_request.text, 'html.parser')

    name_list = parsed_page.find_all('span', {'class': 'green'})  # Search for tag, attribute_dict
    characters = set()
    for name in name_list:
        characters.update([name.get_text().replace('\n', ' ')])  # get_text() strips away all tags
    print(characters)
