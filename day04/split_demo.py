import re

p = re.compile(r'[\s,;]+')
# p = re.compile(r'[\s,\,\;]+')

a = p.split('a,b; ; c    d')

print(a)
#['a', 'b', 'c', 'd']