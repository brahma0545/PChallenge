import re
import urllib2
from bs4 import BeautifulSoup, Comment
response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
page_source = response.read()
soup = BeautifulSoup(page_source, 'html.parser')
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
print("".join(re.findall("[A-Za-z]", comments[1])))
