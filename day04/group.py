import re

content = '{name:"zhangsan",age:"10",hobby:["basktball","football","read"]}'
pattern = re.compile(r'{name:"(\w+)",age:"(\d+)".+')
#正则使用技巧：全串匹配，使用分组获取特定内容，括号两遍的边界一定要指定。

match = pattern.search(content)
print(match.group(0))
#{name:"zhangsan",age:"10",hobby:["basktball","football","read"]}
print(match.group(1))
#zhangsan
print(match.group(2))
#10