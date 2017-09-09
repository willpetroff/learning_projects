"""
Navigating DOM:
.children/.parent
.next_sibling(s)/.previous_sibling(s)
Display tag Attributes
Search by Lambda
"""
import helper_func

from bs4 import BeautifulSoup

url_target = "http://www.pythonscraping.com/pages/page3.html"

page_request = helper_func.get_url(url_target)
if page_request:
    parsed_page = BeautifulSoup(page_request.text, 'html.parser')

    for child in parsed_page.find('table', {'id': 'giftList'}).children:
        print(child)

    for sibling in parsed_page.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(sibling)

    # next_sibling auto-selects the next sibling tag

    for sibling in parsed_page.find('tr', {'id': 'gift5'}).previous_siblings:
        print(sibling)

    # previous_sibling auto-selects the previous sibling tag

    print(parsed_page.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

    print(parsed_page.find("img", {"src": "../img/gifts/img1.jpg"}).attrs)  # returns a dictionary of attributes

    for tag in parsed_page.find_all(lambda tag_item: len(tag_item.attrs) == 2):
        print(tag.attrs)
