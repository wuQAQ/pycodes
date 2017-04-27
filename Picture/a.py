
from selenium import webdriver
import time
import urllib

url = 'http://pic.sogou.com/pics?query=1&di=2&_asf=pic.sogou.com&w=05009900&sut=1486&sst0=1492368726928'

xpath = '//div[@id="imgid"]/ul/li/a/img'

driver = webdriver.Firefox()
driver.maximize_window()

img_url_dic = {}

driver.get(url)

pos = 0
m = 0 
for i in range(10):
	pos += i*500 
	js = "document.documentElement.scrollTop=%d" % pos
	driver.execute_script(js)
	time.sleep(1)   
	
	for element in driver.find_elements_by_xpath(xpath):
		img_url = element.get_attribute('src')
		
		if img_url != None and not img_url_dic.has_key(img_url):
			img_url_dic[img_url] = ''
			m += 1
			ext = img_url.split('.')[-1]
			filename = str(m) + '.' + ext
		
			data = urllib.urlopen(img_url).read()
			f = open('/home/wuqaq/DISK/project/pycodes/Picture/' + filename, 'wb')
			f.write(data)
			f.close()
driver.close()

