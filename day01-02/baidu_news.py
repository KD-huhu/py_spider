import requests

base_url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',

}

params = {
    'rtt': '1',
    'bsst': '1',
    'cl': '2',
    'tn': 'news',
    'rsv_dl': 'ns_pc',
    'word': 'F1',
}

response = requests.get(base_url, headers = headers, params = params)

#print(response.text)
#print(response.status_code)
#print(response.headers)

#保存网页至本地
response_str = response.content.decode('utf-8')
with open ('baidu_news.html', 'w', encoding='utf-8') as fp:
    fp.write(response_str)
