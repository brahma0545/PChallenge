import urllib
import re


def crawl(uri, nothing):
    while True:
        print (uri % nothing)
        page_source = urllib.urlopen(uri % nothing).read()
        nothing = re.search(nothing_rep, page_source).group(1)
        print(nothing)

if __name__ == '__main__':
    uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    nothing = "62712"
    nothing_rep = "and the next nothing is (\d+)"
    crawl(uri, nothing)
    print("first function")
    # nothing = str(int(nothing)/2)
    # crawl(uri, nothing)
    # print ("second function")
