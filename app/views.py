from django.shortcuts import render
import requests
import time
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')

def result(request):
    product_name = request.POST.get("search")
    
    #------------Flipkart's------------#
    
    furl1 = 'https://www.flipkart.com/search?q='
    temp_url = request.POST.get("search")
    temp_url=product_name
    furl2 = str(temp_url)
    furl2 = furl2.replace(" ", "%20")
    furl = furl1 + furl2
    
    
    
    fresponse = requests.get(furl)
    fsoup = BeautifulSoup(fresponse.content, 'html.parser')
    check = fsoup('div', {'class': '_2kHMtA'})
    if len(check) == 0:
        product_containers = fsoup.find_all('div', {'class': '_4ddWXP'})
        
        title = []
        price = []
        rating = []
        image = []
        logo = []
        url= []
        
        
        for container in product_containers:
            ttl = container.find('a', {'class': 's1Q9rs'}).text

            prc = container.find('div', {'class': '_30jeq3'}).text

            rat = container.find('div', {'class': '_3LWZlK'}).text if container.find('div', {
            'class': '_3LWZlK'}) else 'N\A'
            
            img = container.find('img', {'class': '_396cs4'}).get('src') if container.find('img', {'class': '_396cs4'}) else 'N\A'
            
            lg = "https://assets.gadgets360cdn.com/kostprice/assets/img/fk_40_40.png"
            
            ul = 
                
            title.append(ttl)
            price.append(prc)
            rating.append(rat)
            image.append(img)
            logo.append(lg)
            
            
    else:
        product_containers = fsoup.find_all('div', {'class': '_2kHMtA'})
        
        title = []
        price = []
        rating = []
        image = []
        logo = []
        url = []
        
        for container in product_containers:
            ttl = container.find('div', {'class': '_4rR01T'}).text
            
            prc = container.find('div', {'class': '_30jeq3 _1_WHN1'}).text

            rat = container.find('div', {'class': '_3LWZlK'}).text
            
            img = container.find('img', {'class': '_396cs4'}).get('src') if container.find('img', {'class': '_396cs4'}) else 'N\A'
            
            lg = "https://assets.gadgets360cdn.com/kostprice/assets/img/fk_40_40.png"
            
            ul = container.find('a', {'class': '_1fQZEK'}).get('href')
            
            title.append(ttl)
            price.append(prc)
            rating.append(rat)
            image.append(img)
            logo.append(lg)
            
         
         
    fdata = zip(image, title, price, rating, logo)
    
    # ------------Amazon's------------#
    
    aurl1 = 'https://www.amazon.in/s?k='
    aurl2 = furl2.replace("%20", "+")
    aurl = aurl1 + aurl2 
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    aresponse = requests.get(aurl, headers=headers)
    
    asoup = BeautifulSoup(aresponse.text, 'lxml')
    
    adict = {"Title": [], "Price": [], "Rating": []}
    
    products = asoup.find_all('div', {
    'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}) if asoup.find_all(
    'div', {
        'class': 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'}) else asoup.find_all(
    'div', {
        'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})


    title = []
    price = []
    rating = []
    image = []
    logo = []
        
    for product in products:
        ttl = product.find('a',
                         {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).text
        
        if (product.find('span', {'class': 'a-price-whole'})):
            prc = product.find('span', {'class': 'a-price-whole'}).text
        elif (product.find('span', {'class': 'a-size-small'})):
            prc = product.find('span', {'class': 'a-size-small'}).text
        else:
            prc = "NA"
            
        rat = product.find('span', {'class': 'a-icon-alt'}).text.split()[0] if product.find('span', {'class': 'a-icon-alt'}) else "Currently unavailable"
        
        img = product.find('img', {'class': 's-image'}).get('src') if product.find('img', {'class': 's-image'}).get('src') else "Currently unavailable"
        
        lg = "https://assets.gadgets360cdn.com/kostprice/assets/img/amazon_40_40.png"
        
        
        title.append(ttl)
        price.append(prc)
        rating.append(rat)
        image.append(img)
        logo.append(lg)
        
        
    adata = zip(image, title, price, rating, logo)

    zipped = zip(adata, fdata)    
    context = {'data': zipped}        
    return render(request, 'result.html', context)