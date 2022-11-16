from bs4 import BeautifulSoup
import requests
for page in range(1, 2):
    url = 'http://books.toscrape.com/'
    html = requests.get(url+'catalogue/page-'+str(page)+'.html')
    html_soup = BeautifulSoup(html.content, 'html.parser')
    card = html_soup.select('article', class_ = 'product_pod')
    data = []
    for i in card:
        imageLink = i.select_one('img')['src']
        title = i.h3.a['title']
        rating = i.select_one('p')['class']
        price = i.select_one('p', class_ = 'price_color').text
        sep = "\n"
        data.append({
             f'linkGambar': imageLink,
             f'title': title,
             f'rating': rating,
             f'price': price,
             f'':sep
         })
        print(data)
    print("Page ke: " +str(page)+"=====================================")

# from bs4 import BeautifulSoup # import modul beautifulsoup
# import requests # import modul requests
# import urllib.parse # import modul urllib

# urlscrape = urllib.parse.urlsplit("http://books.toscrape.com/")
# urlbase = f"{urlscrape.scheme}://{urlscrape.netloc}/"
# page = "catalogue/page-{p}.html"

# list_halaman = []
# for i in range(1,2):
#     list_halaman.append(urllib.parse.urljoin(urlbase,page.format(p=i)))
    
    
# for page in list_halaman:
#     req = requests.get(page)
#     soup = BeautifulSoup(req.content,"html.parser")
    
#     semuabuku = soup.select('article.product_pod')
#     for buku in semuabuku:
#         gambar = buku.select_one('div.image_container img.thumbnail')
#         judul = buku.select_one('h3.a')
#         rating = buku.select_one('p.star-rating')
#         harga = buku.select_one('div.product_price p.price_color')
        
#         print(
#             f'Gambar: {urllib.parse.urljoin(urlbase,gambar.attrs["src"])}',
#             f'Judul: {judul.attrs["title"]}',
#             f'Rating: {rating.attrs["class"[1]]}',
#             f'Harga: {harga.text.replace["£", ""]}',
#             "\n"
#         )