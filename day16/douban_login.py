import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def get_tracks(distance):
    '''
    获取0.3秒时间间隔下的δS
    :param distance:
    :return:存放间隔距离的列表
    '''
    #移动的速度
    v = 0
    #时间间隔
    t = 0.3
    tracks = []
    #定义当前移动距离
    current = 0
    mid = distance*2/3
    while current<distance:
        if current<mid:
            a = 4
        else:
            a = -3
        v0 = v
        s = v0*t+0.5*a*(t**2)
        tracks.append(round(s))
        current+=s
        v =v0+a*t
    return tracks



def login(user,passwd):
    '''
    登录豆瓣方法
    :param ueser:
    :param passwd:
    :return:
    '''
    base_url = 'https://www.douban.com/'
    #创建driver
    driver = webdriver.Chrome()
    #请求
    driver.get(base_url)
    #登录
    driver.implicitly_wait(10)
    #切入登录框所对应的的ifram
    #如果遇到frame标签（框架标签），记得要切入进去
    driver.switch_to.frame(0)
    #点击密码登录
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    #填充用户名和密码
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
    #点击登录
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    driver.implicitly_wait(10)

    # if 'ZzzP的账户' in driver.page_source:
    #     print('登录成功！')
    # else:
    #     print('登录失败！')
    #     time.sleep(2)
        #解决验证码
        #手动
        # shoudong(driver)
        # 切入
    while not 'ZzzP的账户' in driver.page_source:
        print(1)
        driver.switch_to.frame(0)
        huakuai = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        # click_and_hold就是点击并保持点击
        # perform:鼠标悬浮
        AC(driver).click_and_hold(on_element=huakuai).perform()

        AC(driver).move_to_element_with_offset(to_element=huakuai, xoffset=100, yoffset=0).perform()
        #滑动验证码实现原理模仿人的行为：先加速后减速过程


        # driver.save_screenshot('anc.png')
        time.sleep(3)
        tracks = get_tracks(110)
        print(tracks)
        for s in tracks:
            AC(driver).move_by_offset(xoffset=s,yoffset=0).perform()

        time.sleep(2)
        # 释放鼠标
        AC(driver).release().perform()
        time.sleep(5)




    # time.sleep(10)
def main():
    #用户名
    username = '18524158889'
    #密码
    password = 'zp7512799'
    login(username,password)
if __name__ == '__main__':
    main()