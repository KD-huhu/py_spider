import re

pattern = re.compile(r'([a-z]+) ([a-z]+)',re.I)
#将正则表达式对象编译成pattern对象
#re.I表示忽略大小写

content = 'Hello World Wide Web'
search_out = pattern.match(content)

print(search_out)
#<re.Match object; span=(0, 11), match='Hello World'>
print(search_out.group(0))
#Hello World
print(search_out.group(1))
#Hello
print(search_out.group(2))
#World
print(search_out.span(0))
#(0, 11)
print(search_out.span(1))
#(0, 5)
print(search_out.span(2))
#(6, 11)

