"""
Beautiful Soup: Selecting tags with find_all
"""
import web_scraping_with_python.helper_func as helper_funcs


url_target = "http://www.pythonscraping.com/pages/warandpeace.html"

parsed_page = helper_funcs.get_page(url_target)
if parsed_page:
    name_list = parsed_page.find_all('span', {'class': 'green'})  # Search for tag, attribute_dict
    characters = set()
    for name in name_list:
        characters.update([name.get_text().replace('\n', ' ')])  # get_text() strips away all tags
    print(characters)
