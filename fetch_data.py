"""
new program
"""

# coding: utf-8 


import urllib2
#import html2text

import lxml
from lxml.html.clean import Cleaner

from bs4 import BeautifulSoup

# response=urllib2.urlopen('http://gutenberg.org')
#http://www.gutenberg.org/files/135/135-h/135-h.htm

def load_web_to_text(link='http://www.gutenberg.org/files/135/135-h/135-h.htm',file='out.txt'):
	raw_file='raw_file.txt'

	response=urllib2.urlopen(link)
	html = response.read()
	with open(raw_file,'w+') as text_file: 
		text_file.write(html)

#	cleantext=cleaner.clean_html(lxml.html.parse(link))


	soup_html=BeautifulSoup(html,'html.parser')
	soup_html.script.clear()
	soup_html.option.clear()
	soup_html.p.clear()
	

#	soup_html=BeautifulSoup(html,'html5lib')
#	txt=soup_html.find('div',{'class':'body'})
#E	print txt
	plane_text=soup_html.body.get_text().encode('utf8')
#	plane_text=txt

#	plane_text=cleantext

	with open(file,'w+') as text_file: 
		text_file.write(plane_text)
	return plane_text

def show_param(clear_text):
#	if type(clear_text)=='str':
	words = clear_text.split(' ')

	text_param = (words[0] + '....' + words[len(words)-1]+' len: ' + str(len(words)))

	print text_param.decode('utf8').encode('cp866')

#print (soup.get_text().encode('utf-8'))

'''
sad=0

list_of_words = html.split(' ')

for word in list_of_words:
	if word =='sad':
		sad +=1

print sad
'''

