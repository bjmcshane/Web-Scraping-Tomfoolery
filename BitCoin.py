from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.nytimes.com/section/technology'
keywords = ['Bitcoin','Cryptocurrency','cryptocurrency','Cryptocurrencies','cryptocurrencies']

#creating a connection to the page with urlopen from the module request inside the package urllib
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

count = 0

articles = page_soup.findAll("li", {"class":"css-xta2bx"})
for member in articles:
	interesting = 0
	title = member.article.div.h2.a.text
	summary = member.article.div.p.text
	link = 'https://www.nytimes.com' + member.article.div.h2.a['href']

	#print(title + "\n")
	for kw in keywords:
		#print(kw+"\n")
		if (kw in title) or (kw in summary):
			interesting = 1

	if interesting==1:
		count+=1
		print(title)
		print(link + "\n")


personalTech = page_soup.findAll("li", {"class":"css-xei2dc ekkqrpp3"})
for member in personalTech:
	interesting = 0
	title = member.article.div.h2.a.text
	summary = member.article.div.p.text
	link = 'https://www.nytimes.com' + member.article.div.h2.a['href']

	#print(title + "\n")
	for kw in keywords:
		#print(kw+"\n")
		if (kw in title) or (kw in summary):
			interesting = 1

	if interesting==1:
		count+=1
		print(title)
		print(link + "\n")


extra = page_soup.findAll("li", {"class":"css-xei2dc ekkqrpp3"})
for member in extra:
	interesting = 0
	title = member.article.div.h2.a.text
	summary = member.article.div.p.text
	link = 'https://www.nytimes.com' + member.article.div.h2.a['href']

	#print(title + "\n")
	for kw in keywords:
		#print(kw+"\n")
		if (kw in title) or (kw in summary):
			interesting = 1

	if interesting==1:
		count+=1
		print(title)
		print(link + "\n")





if count == 0:
	print("Didn't find anything about BitCoin :(")