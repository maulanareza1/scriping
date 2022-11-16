from bs4 import BeautifulSoup
import requests


print('Start!')
for page in range(1,2):
    url = 'http://books.toscrape.com/'
    html = requests.get(url+'catalogue/page-'+str(page)+'.html')
    html_soup = BeautifulSoup(html.content, 'html.parser')
    card = html_soup.find_all('article', class_ = 'product_pod')
    data = []
    for i in card:
        imageLink = i.find('img')['src']
        title = i.h3.a['title']
        rating = i.find('p')['class']
        price = i.find('p', class_ = 'price_color').text
        data.append({
             'linkGambar': imageLink,
             'title': title,
             'rating': rating,
             'price': price[slice(1,len(price))]
         })
        print(data)