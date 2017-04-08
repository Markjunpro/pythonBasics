from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self,name,attrs):
		print('sax:start_element:%s,attrs:%s' % (name,str(attrs)))
	def end_element(self,name):
		print('sax:end_element:%s' % name)
	def char_date(self,text):
		print('sax:cahr_date:%s' % text)

xml=r'''<?xml version="1.0"?>
<ol>
	<li><a href="/python">Python</a><?li>
	<li><a href="/ruby">Ruby</a></li>
<ol>
'''

handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_date
parser.Parse(xml)

L=[]
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & date'))
L.append(r'</root>')
return ''. join(L)

