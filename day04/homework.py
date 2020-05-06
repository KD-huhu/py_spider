import re

date_str = ['2019-02-19','92000-1-19','1019-3-32','2019-02-30']

p = re.compile(r'^[1-9]\d{3}-(1[0-2]|0?[1-9])-(3[0-1]|[12]\d|0?[1-9])$')

for i in date_str:
    print(p.search(i))

# 可以判断部分的非法日期，但2-30无法判断
# <re.Match object; span=(0, 10), match='2019-02-19'>
# None
# None
# <re.Match object; span=(0, 10), match='2019-02-30'>