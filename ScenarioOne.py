import urllib.parse 
import urllib.request 

url = 'http://boodelyboo.com'
with urllib.request.urlopen(url) as response:
  content = response.read()
  
 print(content)
