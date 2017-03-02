"""
new program
"""

import urllib2

from bs4 import BeautifulSoup

# response=urllib2.urlopen('http://gutenberg.org')
#http://www.gutenberg.org/files/135/135-h/135-h.htm

def load_web_to_text(link='http://www.gutenberg.org/files/135/135-h/135-h.htm',file='out.txt'):
	response=urllib2.urlopen(link)
	html = response.read()
	soup=BeautifulSoup(html,'html.parser')
	plane_text=soup.get_text().encode('utf-8')
	with open(file,'w+') as text_file: 
		text_file.write(str(plane_text))
	return plane_text

def show_param(clear_text):
#	if type(clear_text)=='str':
	words = clear_text.split(' ')
	text_param = (words[0] + '....' + words[len(words)-1]+' len: ' + str(len(words)))
	return text_param

#print (soup.get_text().encode('utf-8'))

'''
sad=0

list_of_words = html.split(' ')

for word in list_of_words:
	if word =='sad':
		sad +=1

print sad
'''

