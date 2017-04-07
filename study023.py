import base64

s=base64.b64encode('use Base64 in python'.encode('utf-8'))
print(s)
d=base64.b64decode(s).decode('utf-8')
print(d)

s=base64.urlsafe_b64encode('use Base64 in python'.encode('utf-8'))
print(s)
d=base64.urlsafe_b64decode(s).decode('utf-8')
print(d)

