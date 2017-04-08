import hashlib

print('md5 in python hashlib')
md5=hashlib.md5()
md5.update('how to use md5 in python hashlid?'.encode('utf-8'))
print(md5.hexdigest())

print('\nmd5.update in python hashlib ')

md5.update('how to use md5 in'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

print('\nsha1 in python:')
sha1=hashlib.sha1()
sha1.update('how to use sha1 in'.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

