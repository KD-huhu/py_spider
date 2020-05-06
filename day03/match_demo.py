import re

pattern = re.compile(r'\d+')
#将正则表达式对象编译成pattern对象

content = 'one12twothree34four'
search_out1 = pattern.match(content)
search_out2 = pattern.match(content,2,10)
search_out3 = pattern.match(content,3,10)

print(search_out1)
#None
print(type(search_out1))
#<class 'NoneType'>
print(search_out2)
#None
print(search_out3)
#<re.Match object; span=(3, 5), match='12'>
print(search_out3.group(0))
#12
print(search_out3.span(0))
#(3, 5)
print(search_out3.start())
#3
print(search_out3.end())
#5