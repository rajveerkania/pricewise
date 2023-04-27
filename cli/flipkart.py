import requests
from bs4 import BeautifulSoup

furl1 = "https://flipkart.com/search?q="
furl3 = "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
user_input = input("Enter the product name: ")
user_input = user_input.replace(" ", "%20")
furl = furl1 + user_input + furl3
aurl = furl.replace("%20", "+")


flipkart = requests.get(furl).text


fsoup = BeautifulSoup(flipkart, 'lxml')
fphone_urls = fsoup.find_all('a', class_='_1fQZEK')
fphone_name = fsoup.find_all('div', class_='_4rR01T')
fphone_prices = fsoup.find_all('div', class_='_30jeq3 _1_WHN1')
furls = fsoup.find_all('script', id='jsonLD')


j = 0
print("Loading Flipkart's data...\n\n\n")
for i in fphone_name:
    print(f'''
Phone Name: {i.text}
Price: {fphone_prices[j].text}
          ''')
    j += 1



#Amazon's Data Source

# header = { "User-Agent": "<search result of user agent>", } 

# amazon = requests.get(furl, headers = header)
# # print(amazon)
# soup = BeautifulSoup(amazon.content, 'lxml')
# print(soup.prettify())
# phone_names = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
# phone_prices = soup.find_all("span", class_="a-price-whole")
# j = 0
# print("\nLoading Amazon's data...\n\n")
# for i in phone_names:
#     print(f'''
# Title: {i.text.strip()}
# Price: {"₹ " + phone_prices[j].text.strip()}
#           ''')
#     j += 1