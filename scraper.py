import requests
from bs4 import BeautifulSoup

# -------------------- Address To Be Scraped ----------------- # 
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
# ------------ Main Function ----------- # 
def scraper_wiki_citations_needed(URL):
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))

# Would prefer a function that gets soup independently of count/report
# def get_soup(URL):
#     page = requests.get(URL)
#     # print(page.content)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     return soup.prettify()


# -------------------- Count Function -------------------- # 
def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_='noprint Inline-Template Template-Fact')
    print(len(results))

# -------------------- Report Function -------------------- # 
def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_='noprint Inline-Template Template-Fact')
    print(results)
    for item in results:
        print(item.parent.text)

# ------ Function Call ------- #
scraper_wiki_citations_needed(URL)