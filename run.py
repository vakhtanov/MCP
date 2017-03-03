"""
comment
"""

from markov_python.cc_markov import MarkovChain
import fetch_data

link='http://www.e-reading.club/bookreader.php/1020088/Fomina_-_Pritchi._Daosskie%2C_kitayskie%2C_dzenskie.html'
#link='http://www.krotov.info/acts/01/joseph/filon_02.htm'

vocabul=fetch_data.load_web_to_text(link,'voc.txt')

print fetch_data.show_param(str(vocabul))

out_file='out_text.txt'

text_object=MarkovChain(3)
text_object.add_file('voc.txt')
out_text = text_object.generate_text(200)
for i in out_text: 	print type(i),i.decode('cp866')
out_text_j = ' '.join(out_text)
with open(out_file,'w+') as ofile:
	for i in out_text: ofile.write(i+'\n')


#print out_text.decode('utf-8')
#print out_text_j.decode('utf-8')

print 'Error'

