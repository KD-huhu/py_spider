import re

pattern = re.compile(r'\d+')
#定义匹配对象为数字

content = 'one12twothree34four'
search_out = pattern.search(content)
#print(search_out)
#<re.Match object; span=(3, 5), match='12'>
#print(search_out.group(0))
#12
search_out1 = pattern.search(content,10,30)
print(search_out1)
#<re.Match object; span=(13, 15), match='34'>
print(search_out1.group(0))
#34
print(search_out.span())
#(3, 5)