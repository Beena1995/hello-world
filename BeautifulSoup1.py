import urllib
from BeautifulSoup import*
url=raw_input('Enter url:')
html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
tags=soup('a')
for tag in tags:
    print 'TAG:',tag
    print 'URL:',tag.get('href',None)
    print 'Content:',tag.contents[0]
    print 'Attrs:',tag.attrs