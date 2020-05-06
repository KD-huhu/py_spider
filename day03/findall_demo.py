import re

# 将正则表达式编译成一个pattern对象
#1
#pattern = re.compile('we')
#['we', 'we', 'we']

#2
#pattern = re.compile('(w)(e)')
#[('w', 'e'), ('w', 'e'), ('w', 'e')]

#3
pattern = re.compile('(w)e')
#['w', 'w', 'w']

#4
pattern = re.compile('w(e)')
#['e', 'e', 'e']

content = 'we work well welcome'
search_out = pattern.findall(content)

print(search_out)