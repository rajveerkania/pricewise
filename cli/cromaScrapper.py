from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# Set up the browser
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Navigate to the Amazon website and search for a query
url1 = input("Enter the product name: ")
url2 = "https://www.croma.com/searchB?q=query%3Arelevance&text=query"
url = url2.replace("query", url1)
driver.get(url)

# Wait for the search results to load
driver.implicitly_wait(10)

# Get the page source and parse it using BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find the first search result and extract its title, price, and rating
product_list = soup.find_all('li', {'class': 'product-item'})
title=[]
price=[]

for product in product_list:
    ttl = product.find('h3', {'class': 'product-title plp-prod-title'}).find('a').text
    
    prc = product.find('span', {'class': 'amount'})
    
    title.append(ttl)
    price.append(prc)    

# Print the title, price, and rating
print(title)
print(price)
# Clean up
driver.quit()
