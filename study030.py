from urllib import request

with request.urlopen ('https://www.baidu.com') as f:
	date=f.read()
	print('Statu.',f.status,f.reason)
	for k ,v in f.getheaders():
		print('%s:%s' %(k,v))
	print('Date:',date.decode('utf-8'))

