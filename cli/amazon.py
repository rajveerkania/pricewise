import requests
from bs4 import BeautifulSoup

header = { "User-Agent": "<search result of user agent>", } 

url1 = "https://www.amazon.in/s?k="
url2 = input("Enter the keyword: ")
url2 = url2.replace(" ", "+")
url = url1 + url2

amazon = requests.get(url, headers = header)
# print(amazon)
soup = BeautifulSoup(amazon.content, 'lxml')
phone_names = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
phone_prices = soup.find_all("span", class_="a-price-whole")
phone_urls = soup.find_all("a", class_="a-link-normal s-no-outline")
j = 0
k = 2
print("\nLoading Amazon's data...\n\n")
for i in phone_names:
    print(f'''
Title: {i.text.strip()}
Price: {"₹ " + phone_prices[j].text.strip()}
Url: {"More info: " "https://www.amazon.in" + phone_urls[j].get('href')}
          ''')
    j += 1
    k += 1 
    
