import requests
import os
from IPython.display import IFrame

r = requests.get('https://www.ibm.com')
print(r.status_code)
# print(r.request.headers)
# print(r.request.body)
header = r.headers
print(r.headers)

