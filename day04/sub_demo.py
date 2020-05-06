import re

p = re.compile(r'(\w+) (\w+)')

s = 'hello 123,hello 456'
#提前用p去匹配目标串，找到能匹配出来的内容，就是替换找出来的这个内容的。

#使用‘hello world'替换'hello 123'和'hello 456'
print(p.sub(r'hello world',s))
#hello world,hello world

#引用分组
print(p.sub(r'\2 \1',s))
#123 hello,456 hello
