from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
my_url = 'https://www.amazon.in/s/ref=mega_elec_s23_2_1_1_2?rh=i%3Acomputers%2Cn%3A14584411031&ie=UTF8&bbn=976392031'
client = urlopen(my_url)
page_html = client.read()
client.close()
page_soup = soup(page_html, "html.parser")
contains = page_soup.findAll("div", {"class":"s-item-container"})
xx = int(input())
filename = "products1.csv"
f = open(filename, "w")
f.write("Product_Name, Price\n")
for j in range(len(contains)-1):
	cd = contains[j].findAll("div", {"class":"a-row a-spacing-mini"})
	dd = cd[0].div.a.text
	ed = ""
	for i in dd:
		if i == "(":
			break
		ed += i
	cur = cd[1].findAll("span", {"class":"a-size-base a-color-price s-price a-text-bold"})
	junk = cur[0].span.text
	v = cur[0].text
	ss =""
	for i in v:
		if i != ",":
			ss += i
	val = int(ss)
	if val < xx:
		print(ed, end="||")
		print(val)

		f.write(ed + "," + str(val) + "\n")

f.close()