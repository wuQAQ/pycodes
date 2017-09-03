from bs4 import BeautifulSoup
import urllib.request
import socks
from sockshandler import SocksiPyHandler
from urllib.request import urlopen

opener = urllib.request.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 1080))
urllib.request.install_opener(opener)
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)