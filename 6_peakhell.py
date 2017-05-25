import urllib2
import pickle
response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(response)
response.close()
print (data)
for elt in data:
    # print ([e[1] for e in elt])
    print ("".join([e[1] * e[0] for e in elt]))
