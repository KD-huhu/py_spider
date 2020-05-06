import requests
import json
#确定url
base_url = 'https://fanyi.baidu.com/sug'
#准备参数
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://fanyi.baidu.com/',
    'content-length': '9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
data = {
    'kw': 'python',
}
response = requests.post(base_url,headers=headers,data=data)
# print(response.text)
#处理json的方法
json_data = json.loads(response.text)
# print(json_data)
'''
{"errno":0,"data":[{"k":"python","v":"n. \u87d2; \u86ba\u86c7;"},{"k":"pythons","v":"n. \u87d2; \u86ba\u86c7;  python\u7684\u590d\u6570;"}]}
{'errno': 0, 'data': [{'k': 'python', 'v': 'n. 蟒; 蚺蛇;'}, {'k': 'pythons', 'v': 'n. 蟒; 蚺蛇;  python的复数;'}]}
'''
result = ''
for data in json_data['data']:
    result += data['v']+'\n'
print(result)