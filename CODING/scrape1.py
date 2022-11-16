from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <title> Belajar Scrape</title>
</head>

<body>
<p class="judul">Belajar Data Scriping</p>
<p class="paragraf">Ini Adalah Contoh paragraf</p>
<a href="abc.com">Read More</a>
</body>
</html>
'''

html_soup = BeautifulSoup(html,"html.parser")
judul = html_soup.find('p',class_='judul').text
paragraf = html_soup.find('p',class_ ='paragraf').text

print(judul)
print(paragraf)