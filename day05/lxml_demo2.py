from lxml import etree

'''
xml文档的解析方法
'''

# parse 方法就是按照xml的语法要求来进行解析的。
tree = etree.parse('a.html')
# print(tree)
# <lxml.etree._ElementTree object at 0x00000163BC702D08>