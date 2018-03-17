import requests
from bs4 import Beatifulsoup


# web crawler for bucky's website (no longer works)
def trade_spider(max_page):
    page = 1;
    while page <= max_page:
        url = 'https://bucksroom.org/trade/search.php?page=' + str(page)

        # 1 step: get source code using url
        source_code = requests.get(url)

        # 2 step: convert the source code into plain text
        plain_text = source_code.text

        # 3 step: convert plain text into a soup object
        soup = Beatifulsoup(plain_text)

        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "https://buckysroomorg" + link.get('href')
            #print (href)
        page+=1

# think of using sets to not repeat
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = Beatifulsoup(plain_text)

    # pulling out title
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckysroomorg" + link.get('href')
        print(href)

# specify the page number
trade_spider(1)