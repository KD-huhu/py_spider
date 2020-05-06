import re

pattern = re.compile(r'\d+')

content1 = 'hello 123456 789'
content2 = 'one1two2three3four4'

result1 = pattern.finditer(content1)
result2 = pattern.finditer(content2,0,10)

# print(type(result1))
# print(type(result2))

#print(result1)
#print(result2)

for m1 in result1:
    print('matching string:{},position:{}'.format(m1.group(),m1.span()))
for m2 in result2:
    print('matching string:{},position:{}'.format(m2.group(),m2.span()))