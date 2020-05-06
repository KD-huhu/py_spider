import requests

def login():
    #登录界面的url
    login_url = 'http://www.renren.com/PLogin.do'

    #创建一个session（会话）对象：可以记录登录后的状态。
    session = requests.session()
    #用session对象来进行登录操作，这个对象就会记录登录的状态。
    #准备登录请求的参数
    #使用post方法进行登录
    data = {
        'email': '18888923239',
        'password': '19990416wang',
    }
    #登录
    session.post(login_url,headers = headers, data = data)
    return session

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    }
    session = login()
    index_url = 'http://www.renren.com/974255453/profile'
    response = session.get(index_url,headers = headers)
    if '澄江' in response.text:
        print("登录成功！")
    else:
        print("登录失败！")