from bs4 import BeautifulSoup
import requests

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

url = "https://www.chrono24.ca/omega/speedmaster--mod74.html"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

#listings = soup.find_all("div", {"class":"js-article-item-container article-item-container wt-search-result article-image-carousel"})

def scrape_listing(listing):
    model = listing.find("div", {"class": "text-sm text-sm-md text-bold text-ellipsis"})
    make = listing.find("div", {"class": "text-sm text-sm-md text-ellipsis m-b-2"})
    price = listing.find_all("div", {"class": "text-bold"})[1]
    currency = listing.find("span", {"class": "currency"})
    shipping = listing.find("div", {"class": "text-muted text-sm"})
    location = listing.find("button", {"class": "js-tooltip d-flex flex-column align-items-center relative"})['data-content']

    print(model.text.strip("\n"))
    print(make.text.strip("\n"))
    print(price.text.strip("\n"))
    print(currency.text.strip("\n"))
    print(shipping.text.strip("\n"))
    print(location.strip("\n"))
    
    print("\n")


urls = [
    "https://www.chrono24.ca/rolex/index.htm#gref", 
    "https://www.chrono24.ca/omega/speedmaster--mod74.html",
    "https://www.chrono24.ca/search/index.htm?query=shunbun&dosearch=true&searchexplain=1&watchTypes=&accessoryTypes="
]

for url in urls:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    listings = soup.find_all("div", {"class":"js-article-item-container article-item-container wt-search-result article-image-carousel"})
    for listing in listings:
        scrape_listing(listing)