fp = open('homework.py','r',encoding='utf-8')

#enumerate(
    #可迭代对象
    #索引的开始值，默认是0
# )

for i,line in enumerate(fp, 1):
    print(i, line, sep=':')