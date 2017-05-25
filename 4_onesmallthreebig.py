import re
import urllib2
from bs4 import BeautifulSoup, Comment
response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
page_source = response.read()
soup = BeautifulSoup(page_source, 'html.parser')
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
print ("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", comments[0])))
