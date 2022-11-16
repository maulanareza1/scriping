import requests
from bs4 import BeautifulSoup
import urllib.parse

url_scrape = urllib.parse.urlsplit("https://books.toscrape.com/")  # <scheme>://<netloc>/<path>?<query>#<fragment>
basis_url = f"{url_scrape.scheme}://{url_scrape.netloc}/"
halaman = "/catalogue/page-{i}.html"


daftar_halaman = []
for x in range(1,4):
    daftar_halaman.append(urllib.parse.urljoin(basis_url, halaman.format(i=x)))


for halaman in daftar_halaman:
    permintaan = requests.get(halaman)
    soup = BeautifulSoup(permintaan.content, "html.parser")

    semua_buku = soup.select("article.product_pod")
    for buku in semua_buku:
        gambar = buku.select_one("div.image_container img.thumbnail")
        judul = buku.select_one("h3 a")
        rating = buku.select_one("p.star-rating")
        harga = buku.select_one("div.product_price p.price_color")
        print(
            f"gambar: {urllib.parse.urljoin(basis_url,gambar.attrs['src'])}",  # gambar buku: https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg
            f"judul: {judul.attrs['title']}",  # judul buku: A Light in the Attic
            f"rating: {rating.attrs['class'][1]}",  # rating: Three
            f"harga: {harga.text.replace('£','')}",  # harga: 51.77
            "\n",
            sep="\n",
        )
    print('')
    print("Halaman ke- "+str(halaman))
    print("")