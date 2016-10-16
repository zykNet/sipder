import os
print os.getcwd()
url='http://tieba.baidu.com/p/4297917156?see_lz=1&pn=' #1~7
import urllib2
import codecs
from bs4 import BeautifulSoup
urls={}
def save(a,name):
	with codecs.open(name,'a',"utf-8-sig") as file:
		file.write(a)
		file.write('\r\n')
def deal(soup,text_name):
	tags = soup.findAll(name='div', attrs={'class': 'd_post_content j_d_post_content '})#a
	for texts in tags:
		for text in texts.strings:
			save(text,text_name)

# main 
for index in range(7):
	urls[index]=url+str(index+1)
	content = urllib2.urlopen(urls[index]).read()
	soup = BeautifulSoup(content,"html.parser")
	txt_name='Bike-page'+str(index+1)+'.txt'
	deal(soup,txt_name)
