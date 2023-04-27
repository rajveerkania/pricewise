from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text



soup = BeautifulSoup(html_text, 'lxml')
phone_urls = soup.find_all('a', class_='_1fQZEK')
phone_name = soup.find_all('div', class_='_4rR01T')
phone_prices = soup.find_all('div', class_='_30jeq3 _1_WHN1')
urls = soup.find_all('script', id ='jsonLD')



    
j = 0    
for i in phone_name:    
    print(f'''
Phone Name: {i.text}
Price: {phone_prices[j].text}
More info: {phone_urls[j].get('href')}
          ''')
    j += 1 

# phones_prices = prices.text


# From local file


# with open('index.html', 'r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'html.parser')
#     tags = soup.find('h1')
#     print(tags)
