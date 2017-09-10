"""
Navigating DOM:
.children/.parent
.next_sibling(s)/.previous_sibling(s)
Display tag Attributes
Search by Lambda
"""
import web_scraping_with_python.helper_func as helper_funcs


url_target = "http://www.pythonscraping.com/pages/page3.html"

parsed_page = helper_funcs.get_page(url_target)
if parsed_page:
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
