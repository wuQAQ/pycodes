#coding=utf-8
from selenium import webdriver
import time
#构造数据，城市分别是北京、天津、石家庄、太原、济南、沈阳、呼和浩特、郑州
city_id=['101010100','101030100','101090101','101100101','101120101','101070101','101080101','101180101']
def getcityid(city):
    if city=='beijing':
        return city_id[0]
    elif city=='tianjin':
        return city_id[1]
    elif city=='shijiazhuang':
        return city_id[2]
    elif city=='taiyuan':
        return city_id[3]
    elif city=='jinan':
        return city_id[4]
    elif city=='shenyang':
        return city_id[5]
    elif city=='huhehaote':
        return city_id[6]
    else:
        return city_id[7]
#获取天气情况数据
def getweather(city):
    try:
        browser=webdriver.PhantomJS()
        print("城市："+city)
        #构造url
        url="http://www.weather.com.cn/weather1d/"+getcityid(city)+".shtml"
        browser.get(url)
        browser.implicitly_wait(10)
        #构造列表
        weatherlist=[]
        #获取当前系统时间
        datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        weatherlist.append(str(datetime))
        #获取天气情况
        weaElement=browser.find_element_by_xpath('//*[@id="today"]/div[2]/ul/li[1]/p[1]')
        weatherlist.append(str(weaElement.text))
        #获取温度情况
        tempElement=browser.find_element_by_xpath('//*[@id="today"]/div[2]/div/div[4]/span')
        weatherlist.append(str(tempElement.text))
        #获取风向
        windElement=browser.find_element_by_xpath('//*[@id="today"]/div[2]/div/div[3]/span')
        weatherlist.append(str(windElement.text))
        # 获取风速
        windspeedElement = browser.find_element_by_xpath('//*[@id="today"]/div[2]/div/div[3]/em')
        weatherlist.append(str(windspeedElement.text))
        #获取湿度
        wetElement = browser.find_element_by_xpath('//*[@id="today"]/div[2]/div/div[2]/em')
        weatherlist.append(str(wetElement.text))
        print("系统时间、天气情况、温度、风向、风速、湿度")
        print(weatherlist)
    except Exception as e:
        print("获取天气数据出现异常！将在一分钟之后重试……")
        print("Exception："+str(e))
        time.sleep(60)
        getweather(city)

#主函数
while(True):
    getweather("beijing")
    getweather("tianjin")
    getweather("shijiazhuang")
    getweather("taiyuan")
    getweather("jinan")
    getweather("shenyang")
    getweather("huhehaote")
    getweather("zhengzhou")
    #休息一小时
    time.sleep(3600)