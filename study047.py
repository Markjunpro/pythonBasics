#server.py

from wsgiref.simple_server import make_server
from study046 import application 

httpd=make_server('',8000,application )
print('Servering HTTP on part 8000...')
httpd.serve_forever()

