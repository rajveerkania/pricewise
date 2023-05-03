from django.shortcuts import render
import requests
import time
from bs4 import BeautifulSoup
from django.core.paginator import Paginator


def homeView(request):
    return render(request, 'index.html')


def resultView(request):
    query = request.GET.get("q")
    sort_by = request.GET.get("s") if request.GET.get('s') else "relevanceblender"

    fdata = list(flipkartResults(query, sort_by))
    adata = list(amazonResults(query, sort_by))

    products = zip(adata, fdata)
    all_products = adata + fdata
    final_products = []

    if sort_by == 'price-asc-rank':
        final_products = sorted(all_products, key=lambda x: x[1])
    elif sort_by == 'price-desc-rank':
        final_products = sorted(all_products, key=lambda x: x[1], reverse=True)
    else:
        for amazonProduct, flipkartProduct in products:
            final_products.append(amazonProduct)
            final_products.append(flipkartProduct)

    paginator = Paginator(final_products, 12)    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'query': query,
        'sort_by': sort_by,
    }
    return render(request, 'result.html', context)


def flipkartResults(query, sort_by):
    titles = []
    prices = []
    images = []
    links = []
    ratings = []
    logos = []

    if query:
        if sort_by == 'relevanceblender':
            sort_by = 'relevance'
        elif sort_by == 'price-asc-rank':
            sort_by = 'price_asc'
        elif sort_by == 'price-desc-rank':
            sort_by = 'price_desc'
        elif sort_by == 'date-desc-rank':
            sort_by = 'recency_desc'
        url = 'https://www.flipkart.com/search?q=' + query + "&sort=" + sort_by

        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')
        

        products = soup.find_all('div', {'class': '_2kHMtA'}) if soup.find_all(
            'div', {'class': '_2kHMtA'}) else soup.find_all(
                'div', {'class': '_4ddWXP'})
            
        if len(products) == 0:
            products = soup.find_all('div', {'class': '_1xHGtK _373qXS'})
            
            for product in products:
                title = product.find('div', {'class': '_2WkVRV'}).get_text() + ' ' + product.find('a', {'class': 'IRpwTa'}).get_text()
                
                price = product.find('div', {'class': '_30jeq3'}).get_text()
                
                rating = "N\A"
                
                image = product.find('img', {'class': '_2r_T1I'}).get('src')
                
                link = product.find('a', {'class': '_2UzuFa'}).get('href')
                
                logo = "https://assets.gadgets360cdn.com/kostprice/assets/img/fk_40_40.png"
                
                titles.append(title)
                prices.append(price)
                ratings.append(rating)
                images.append(image)
                links.append("https://www.flipkart.com" + link)
                logos.append(logo)  
        
        else:
            for product in products:
                title = product.find('div', {
                    'class': '_4rR01T'
                }).get_text() if product.find(
                    'div', {'class': '_4rR01T'}) else product.find(
                        'a', {
                            'class': 's1Q9rs'
                        }).get_text()
                price = product.find('div', {
                    'class': '_30jeq3 _1_WHN1'
                }).get_text() if product.find(
                    'div', {'class': '_30jeq3 _1_WHN1'}) else product.find(
                        'div', {
                            'class': '_30jeq3'
                        }).get_text()
                rating = product.find('div', {
                    'class': '_3LWZlK'
                }).get_text() if product.find('div',
                                              {'class': '_3LWZlK'}) else "N\A"
                image = product.find('img', {'class': '_396cs4'}).get('src')
                link = product.find('a', {
                    'class': '_1fQZEK'
                }).get('href') if product.find(
                    'a', {'class': '_1fQZEK'}) else product.find(
                        'a', {
                            'class': '_2rpwqI'
                        }).get('href')
                logo = "https://assets.gadgets360cdn.com/kostprice/assets/img/fk_40_40.png"

                titles.append(title)
                prices.append(price)
                ratings.append(rating)
                images.append(image)
                links.append("https://www.flipkart.com" + link)
                logos.append(logo)   
            
    results = zip(titles, prices, images, links, ratings, logos)

    return results


def amazonResults(query, sort_by):
    titles = []
    prices = []
    images = []
    links = []
    ratings = []
    logos = []

    if query:
        url = 'https://www.amazon.in/s?k=' + query + "&s=" + sort_by
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')

        products = soup.find_all(
            'div', {
                'class':
                'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
            }
        ) if soup.find_all(
            'div', {
                'class':
                'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
            }
        ) else soup.find_all(
            'div', {
                'class':
                'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'
            })

        for product in products:
            title = product.find(
                'a', {
                    'class':
                    'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'
                })
            
            if (product.find('span', {'class': 'a-price-whole'})):
                price = product.find('span', {
                    'class': 'a-price-whole'
                }).get_text()
            elif (product.find('span', {'class': 'a-size-small'})):
                price = product.find('span', {
                    'class': 'a-size-small'
                }).get_text()
            else:
                price = "NA"
            image = product.find('img', {'class': 's-image'}) if product.find(
                'img', {'class': 's-image'}) else "NA"
            link = product.find(
                'a', {
                    'class':
                    'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'
                })
            rating = product.find('span', {
                'class': 'a-icon-alt'
            }).get_text() if product.find('span',
                                          {'class': 'a-icon-alt'}) else "N\A"
            logo = "https://assets.gadgets360cdn.com/kostprice/assets/img/amazon_40_40.png"

            titles.append(title.get_text())
            links.append("https://www.amazon.in" + link.get('href'))
            prices.append("₹" + price)
            images.append(image.get('src'))
            ratings.append(rating)
            logos.append(logo)

    results = zip(titles, prices, images, links, ratings, logos)

    return results