import requests
from bs4 import BeautifulSoup

url = "https://www.reliancedigital.in/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find all products on the homepage
products = soup.find_all('div', class_='product-list__item__details')

# Extract title and price for each product
for product in products:
    title = product.find('div', class_='product-list__item__details__title').text.strip()
    price = product.find('div', class_='product-list__item__details__price').text.strip()
    print("Title: " + title)
    print("Price: " + price)
