import requests
import json

def main(kw):
    base_url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': kw
    }
    #求取data数组转换为字符串的长度
    data_len = len(str(data))

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://fanyi.baidu.com/',
        #将data字符串长度，从整型转换为字符串
        'content-length': str(data_len),
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    response = requests.post(base_url, headers = headers, data = data)

    #print(response.text)
    '''
    {"errno":0,"data":[{"k":"python","v":"n. \u87d2; \u86ba\u86c7;"},{"k":"pythons","v":"n. \u87d2; \u86ba\u86c7;  python\u7684\u590d\u6570;"}]}
    '''

    #处理异步请求json数据
    json_data = json.loads(response.text)

    #print(json_data)
    '''
    n. 蟒; 蚺蛇;
    n. 蟒; 蚺蛇;  python的复数;
    '''

    results = ''
    for data in json_data['data']:
        results += data['v'] + '\n'
    print(results)

if __name__ == '__main__':
    #kw = 'china'
    kw = input("Input a word： \n")
    main(kw)
