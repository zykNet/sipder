urls=[
'http://www.eefocus.com/embedded/340974/r0',
'http://www.eefocus.com/embedded/341017/r0',
'http://www.eefocus.com/mcu-dsp/341681/r0 ',
'http://www.eefocus.com/embedded/341982/r0',
'http://www.eefocus.com/mcu-dsp/342745/r0 ',
'http://www.eefocus.com/embedded/343177/r0',
'http://www.eefocus.com/embedded/343605/r0',
'http://www.eefocus.com/embedded/344046/r0',
'http://www.eefocus.com/embedded/344555/r0',
'http://www.eefocus.com/embedded/344801/r0',
'http://www.eefocus.com/embedded/345349/r0',
'http://www.eefocus.com/embedded/345720/r0',
'http://www.eefocus.com/embedded/346196/r0',
'http://www.eefocus.com/embedded/346913/r0',
'http://www.eefocus.com/embedded/347457/r0',
'http://www.eefocus.com/embedded/347865/r0',
'http://www.eefocus.com/embedded/348178/r0',
'http://www.eefocus.com/embedded/348598/r0',
'http://www.eefocus.com/embedded/349053/r0',
'http://www.eefocus.com/embedded/349397/r0',
'http://www.eefocus.com/embedded/350389/r0'
]
import urllib2
import codecs
from bs4 import BeautifulSoup
def deal(soup,txt_name):
	# print txt_name
	pdb.set_trace()
	with codecs.open(txt_name,'w+',"utf-8-sig") as file:
		tags = soup.findAll(name='div', attrs={'class': 'article-body'})#a
		p_all=tags[0].find_all(name='p')#b
		for p in p_all:
			for content in p.strings:
				try:
					
					#print unicode(content.string)
					file.write(unicode(content.string))
				except:
					pass
for index,url in enumerate(urls):
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	txt_name=str(index)+'.txt'
	deal(soup,txt_name)
def merge():
	for index in xrange(21):
		name=str(index)+'.txt'
		with codecs.open('all_merge','a',"utf-8-sig") as filea:
			print name
			with codecs.open(name,'r',"utf-8-sig") as file:
				text=file.read()
				filea.write(text) 
