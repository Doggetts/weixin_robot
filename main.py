from urllib import request
from urllib import parse
from urllib.request import urlopen
import urllib3,json,urllib
url = "http://open.iciba.com/dsapi/"
#result = urllib.request.urlopen(url)
result = urllib.request.urlopen(url)
jsonarr = json.loads(result.read())
print (jsonarr)
print("ok ")