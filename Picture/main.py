import urllib
import re

url = "http://tieba.baidu.com/p/2336739808"
html = urllib.urlopen(url)
content = html.read()
html.close()

img_tag = re.compile(r'class="BDE_Image" src="(.+?\.jpg)"')
img_links = re.findall(img_tag, content)

img_counter = 0
for img_link in img_links:
    img_name = '%s.jpg' % img_counter
    urllib.urlretrieve(img_link, "/home/wuqaq/DISK/project/pycodes/Picture/%s" %img_name)
    img_counter += 1