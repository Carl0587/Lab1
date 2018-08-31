# Carlos Ortega
# Capstone Lab1
# DataFromWeb Program
#08/30/18

import webbrowser
import json
from urllib.request import urlopen

print('lets open a website')

webSite = input('Please enter a website URL')
era = input("Type a year, month, and day like 20150613:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (webSite,era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy:", old_site)
    print("It should appear in your browser now")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding it", webSite)