import re

# s = "<html><h1>正则表达式</h1></html>"
# pattern = re.compile(r'<(html)><(h1)>(.*?)</\2></\1>')
# match = pattern.search(s)
# print(match.group(3))


# pattern = re.compile(r'ab{2,5}')
#['abbb']

# pattern = re.compile(r'ab{2,5}?')
#['abb']

# pattern = re.compile(r'ab??')
#['a']

# result = pattern.findall('abbbc')
# print(result)

s = 'aa<div>test1</div>bb<div>test2</div>cc'
# pattern = re.compile('<div>.*</div>')
#['<div>test1</div>bb<div>test2</div>']
pattern = re.compile('<div>.*?</div>')
#['<div>test1</div>', '<div>test2</div>']
result = pattern.findall(s)
print(result)