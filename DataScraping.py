#First of all you need to install beatifulSoup which helps you with HTML

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')#Enter the site you want
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('URL:',tag.get('href', None))
    print('Contents:', tag.contents[0])
    sum += int(tag.contents[0])
#    print('Attrs:', tag.attrs)

print(sum)
