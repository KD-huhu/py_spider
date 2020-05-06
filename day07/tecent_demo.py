import os
import requests
from excel_utils2.excel_write import ExcelUtils

def main():
    # 确定基础url
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1587961275244&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',

    }
    for i in range(1,6):
        response = requests.get(base_url.format(i), headers = headers)
        # print(response.text)
        json_data = response.json()
        infors = json_data['Data']['Posts']
        if os.path.exists(filename):
            ExcelUtils.write_to_excel_append(filename,'tecent',infors)
        else:
            ExcelUtils.write_to_excel(filename,'tecent',infors)


if __name__ == '__main__':
    filename = '腾讯招聘信息.xls'
    main()