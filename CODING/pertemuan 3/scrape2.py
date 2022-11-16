from bs4 import BeautifulSoup
import requests

html = requests.get("http://localhost:8000/index.html")
html_soup = BeautifulSoup(html.content,"html.parser")
judul = html_soup.find('p',class_='judul').text
paragraf = html_soup.find('p',class_ ='paragraf').text

print(judul)
print(paragraf)