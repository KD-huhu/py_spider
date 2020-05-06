import requests

def login():
    base_url = 'https://www.yuque.com/yishengaiai'

    headers = {
        'cookie': 'lang=zh-cn; UM_distinctid=1716bf18ff82db-023293f332e3c4-3f6b4b04-144000-1716bf18ff930d; ctoken=_mhtXOEnVQ-Eqztj19aPvBmf; CNZZDATA1272061571=975046810-1586649024-https%253A%252F%252Fwww.baidu.com%252F%7C1587212963; _TRACERT_COOKIE__SESSION=7ba9fdd0-ab2c-4a40-9f2a-c54c6ae46bb1; _yuque_session=YCpducVLOzf2iclfUmc4dm_cz99jig-7UpR8X-xot8V7cr2HAVckhYWJ90Bj613KnSB9-bnlztp0Yug_AVsM2g==; tree=a385%01feb452a4-c6c5-48f5-aa73-c0673aa455c6%018',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    }

    response = requests.get(base_url,headers = headers)
    #print(response.text)
    if 'ttbrd' in response.text:
        return True
    else:
        return False

if __name__ == '__main__':
    result = login()
    if result:
        print("登录成功！")
    else:
        print("登录失败！")