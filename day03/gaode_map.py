import requests
import time

def getcitycode():
    citycode = []
    # 确定url
    base_url = 'https://www.amap.com/service/cityList'
    # 发送请求
    response = requests.get(base_url, headers = headers)
    # 解析json数据
    json_data = response.json()
    #print(json_data)
    for data in json_data['data']['cityData']['hotCitys']:
        citycode.append((data['adcode'],data['name']))
    return citycode

def get_weather(adcode,city_name):
    '''
       获取城市天气
       :param adcode:
       :return:
    '''
    base_url = 'https://www.amap.com/service/weather?adcode={}'.format(adcode)
    response = requests.get(base_url, headers = headers)
    time.sleep(2)
    json_data = response.json()
    #去除第一个全国的城市这一个无用信息
    if json_data['data']['result'] == 'true':
        weather_name = json_data['data']['data'][0]['forecast_data'][0]['weather_name']
        max_temp = json_data['data']['data'][0]['forecast_data'][0]['max_temp']
        min_temp = json_data['data']['data'][0]['forecast_data'][0]['min_temp']
        #print(json_data)
        item = {}
        item['城市'] = city_name
        item['最高气温'] = max_temp
        item['最低气温'] = min_temp
        print(item)

def main():
    city_code = getcitycode()
    # 获取每个城市天气信息。
    for inf in city_code:
        adcode = inf[0]
        city_name = inf[1]
        get_weather(adcode,city_name)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    main()