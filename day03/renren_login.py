import requests

def login():
    base_url = 'http://www.renren.com/974255453/profile'

    headers = {
        'Cookie': 'anonymid=k95lrjhh-acscn2; depovince=HEN; jebecookies=8b1ee7ec-2a76-4360-bf00-5819da3cb243|||||; _r01_=1; JSESSIONID=abcWNvDjLbXJl-xr5rngx; ick_login=61cd9c80-9701-468e-b89b-c35960950732; taihe_bi_sdk_uid=7a9b5a5c305fd46c540802df9f3283c4; taihe_bi_sdk_session=dc37380ab93323436eb459b075d69e8b; _de=B08847BA131735432B0DF8B67AF8DF30; p=c13a0baf4e941d8b15e16ea4de74053c3; first_login_flag=1; ln_uact=18888923239; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=3db56cd54534e0f96f75429cd5e9a3e13; societyguester=3db56cd54534e0f96f75429cd5e9a3e13; id=974255453; xnsid=72b7f144; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=024ea332-90c2-4bf3-b63e-7c171fdf9792%7Cdab91c4418fa5d04996c24766859f5fb%7C1587213245323%7C1%7C1587213246075; jebe_key=024ea332-90c2-4bf3-b63e-7c171fdf9792%7Cdab91c4418fa5d04996c24766859f5fb%7C1587213245323%7C1%7C1587213246077',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    }

    response = requests.get(base_url,headers = headers)
    #print(response.text)
    if '澄江' in response.text:
        return True
    else:
        return False

if __name__ == '__main__':
    result = login()
    if result:
        print("登录成功！")
    else:
        print("登录失败！")