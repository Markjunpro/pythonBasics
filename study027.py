from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
	for line in page:
		print(line)

print('\n')

@contextmanager
def closing(thing):
	try :
		yield thing
	finally :
		thing.close()
		
