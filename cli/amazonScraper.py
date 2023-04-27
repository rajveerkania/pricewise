import requests
from bs4 import BeautifulSoup

# specify the URL of the Amazon search results page
url = 'https://www.amazon.in/s?k=iphone'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)

# parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'lxml')

products = soup.find_all('div', {
    'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}) if soup.find_all(
    'div', {
        'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}) else soup.find_all(
    'div', {
        'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})

for product in products:
    title = product.find('a',
                         {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    price = product.find('span', {'class': 'a-price-whole'}) if product.find('span', {
        'class': 'a-price-whole'}) else product.find('span', {'class': 'a-size-small'})
    rating = product.find('span', {'class': 'a-size-medium a-color-base a-text-beside-button a-text-bold'}) if product.find('span', {'class': 'a-size-medium a-color-base a-text-beside-button a-text-bold'}) else "Currently unavailable"
    
    print(f'{title.get_text()}')
    print(f'₹{price.get_text()}')
    print(f'{price.get_text()}\n')