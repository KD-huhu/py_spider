import requests
import os

def main(kw):
    base_url = 'https://tieba.baidu.com/f?'
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.162Safari / 537.36',
    }

    #调用OS模块创建文件夹
    filename = './贴吧/' + kw
    if not os.path.exists(filename):
        os.mkdir(filename)

    #循环生成params数组内容
    for i in range(10):
        pn = i*50
        params = {
            'kw': kw,
            'ie': 'utf - 8',
            'pn': pn,
        }
        response = requests.get(base_url,headers = headers, params = params)
        with open(filename + '/' + str(i+1) + '.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)

if __name__ == '__main__':
    kw = 'F1'
    main(kw)
