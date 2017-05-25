# import re
# from urllib.request import urlopen
import bz2
from urllib.parse import unquote_plus, unquote_to_bytes, quote_plus
from urllib.request import Request, urlopen
from xmlrpc.client import ServerProxy
num = '12345'
info = ''
# while(True):
#     h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + num)
#     raw = h.read().decode('utf-8')
#     print(raw)
#     cookie = h.getheader("Set-Cookie")
#     print(cookie)
#     info += re.search('info=(.*?);', cookie).group(1)
#     print(info)
#     match = re.search('the next busynothing is (\d+)', raw)
#     print(match)
#     if match == None:
#         break
#     else:
#         num = match.group(1)
#     print(num)

res = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
result = unquote_to_bytes(res.replace("+", " "))
print(result)
print(bz2.decompress(result).decode())
conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.phone("Leopold"))


url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = Request(url, headers={"Cookie": "info="+quote_plus(msg)})
print(urlopen(req).read().decode())
