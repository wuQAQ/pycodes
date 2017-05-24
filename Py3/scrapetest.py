import urllib.request
import socks
from sockshandler import SocksiPyHandler

opener = urllib.request.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 1080))
urllib.request.install_opener(opener)
r=urllib.request.urlopen("http://pythonscraping.com/pages/page1.html")
print(r.read())