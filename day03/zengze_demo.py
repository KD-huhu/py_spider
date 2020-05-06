import re
'''
正则表达式中r的作用
'''

#我们需要打印出c:\a\b\c
#正斜杠
#反斜杠\---就表示转移字符串\n

path1 = 'c:\a\b\c'
print(path1)
#c:\c
path2 = 'c:\\a\\b\c'
print(path2)
#c:\a\b\c
path3 = r'c:\a\b\c'
print(path3)
#c:\a\b\c