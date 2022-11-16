from bs4 import BeautifulSoup
import requests

try:
    for page in range (1,10):
        html = requests.get('http://quotes.toscrape.com/page/' +str(page))
        html_soup = BeautifulSoup(html.content, 'html.parser')
        semua_quote = html_soup.find_all('div', class_='quote')
        for q in semua_quote:
            data_quote = q.find('span', class_='text').text
            data_author = q.find('small', class_='author').text
            
            print(data_quote)
            print(data_author)
        print("Page ke: " +str(page)+"=====================================")        
except Exception as err:
    print(f'Terjadi Kesalahan : {err}')
