import time
from selenium import webdriver

'''
selenium基础操作
'''

# 1、创建一个驱动
# 无界面的
# driver = webdriver.PhantomJS()

# 有界面的Chrome
driver = webdriver.Chrome()
# 火狐浏览器也支持selenium
# driver = webdriver.Firefox()

# 2、请求url
driver.get('http://www.baidu.com/')

# 3、可以通过dirver对象对页面进行一些操作。
# 获取页面元素

# 通过id属性查找
# driver.find_element_by_id()

# 通过xpath路径查找
# driver.find_element_by_xpath()

# 通过css选择器查找
# driver.find_element_by_css_selector()

# 定位输入框
input_ = driver.find_element_by_id('kw')
print(input_)
#<selenium.webdriver.remote.webelement.WebElement
# 返回一个 WebElement 对象
input_.send_keys(u'python爬虫')

# 查看元素的位置
# print(input_.location)
# 查看元素大小
# print(input_.size)

# 截屏
driver.save_screenshot('beforeclick.png')
# 点击
# 通过寻找到搜索按钮的span标签，进行点击操作
driver.find_element_by_xpath('//*[@id="form"]/span[2]').click()
time.sleep(2)

# 关闭选项卡
driver.close()
# 关闭浏览器
driver.quit()