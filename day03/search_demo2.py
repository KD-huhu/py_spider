import re

pattern = re.compile(r'\d+')
#定义匹配对象为数字

content = 'hello 123456 789'
search_out = pattern.search(content)

print(search_out)
#<re.Match object; span=(6, 12), match='123456'>
print(search_out.group())
#123456
print(search_out.span())
#(6, 12)