import requests
from bs4 import BeautifulSoup

url1 = 'https://www.flipkart.com/search?q='
url2 = input('Enter the product name: ')
url2  = url2.replace(" ", "%20")
url = url1 + url2

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

check = soup('div', {'class': '_2kHMtA'})
if len(check) == 0:
    product_containers = soup.find_all('div', {'class': '_4ddWXP'})
    
    for container in product_containers:
        title = container.find('a', {'class': 's1Q9rs'}).text
        
        price = container.find('div', {'class': '_30jeq3'}).text
        
        rating = container.find('div', {'class': '_3LWZlK'}).text if container.find('div', {
        'class': '_3LWZlK'}) else 'N\A'
        
        
        print(f'\n\nTitle: {title} \nPrice: {price} \nRating: {rating} \n\n')
        
    
else:
    product_containers = soup.find_all('div', {'class': '_2kHMtA'})

    for container in product_containers:
        title = container.find('div', {'class': '_4rR01T'}).text
        
        price = container.find('div', {'class': '_30jeq3 _1_WHN1'}).text
        
        rating = container.find('div', {'class': '_3LWZlK'}).text
        
        
        print(f'\n\nTitle: {title} \nPrice: {price} \nRating: {rating} \n\n')
