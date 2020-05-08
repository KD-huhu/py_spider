import time

import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree

# def main():ders=headers)
    # print(response.content.decode('gbk'))
    # response = requests.get(base_url,hea



if __name__ == '__main__':
    base_url = 'http://www.52bqg.com/book_84329/'
    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    driver = webdriver.Chrome()
    driver.get(base_url)
    # time.sleep(10)
    driver.implicitly_wait(10)
    # wait = WebDriverWait(driver,20)
    # wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="list"]/dl/dd[1]/a')))
    # js = 'var _hmt = _hmt || [];(function () {var hm = document.createElement("script");hm.src = "//hm.baidu.com/hm.js?cec763d47d2d30d431932e526b7f1218";var s = document.getElementsByTagName("script")[0];\
    #         s.parentNode.insertBefore(hm, s);\
    #     })();'
    # driver.execute_script(js)
    # js2 = 'bd_push();addvisit("84329");'
    # driver.execute_script(js2)
    # driver.implicitly_wait(10)
    target = driver.find_element_by_id("list")
    # 拖动到可见的元素去
    driver.execute_script("arguments[0].scrollIntoView();", target)
    # js = "var q=document.documentElement.scrollTop=10000"
    # driver.execute_script(js)
    response = driver.page_source
    # driver.quit()
    print(response)
    # main()