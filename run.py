"""
comment
"""

from markov_python.cc_markov import MarkovChain
import fetch_data

vocabul=fetch_data.load_web_to_text('http://www.krotov.info/acts/01/joseph/filon_02.htm','voc.txt')

print fetch_data.show_param(str(vocabul))

out_file='out_text.txt'

text_object=MarkovChain(3)
text_object.add_file('voc.txt')
out_text = text_object.generate_text(200)
out_text_j = ' '.join(out_text)
with open(out_file,'w+') as ofile:
	ofile.write(out_text_j)

try:
	print out_text.decode('utf-8')
	print out_text_j.decode('utf-8')
except:
	print 'error'.encode('utf-8')