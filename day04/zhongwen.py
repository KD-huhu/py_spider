import re

title = '你好，hello，世界'

pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(title)

print(result)
#['你好', '世界']