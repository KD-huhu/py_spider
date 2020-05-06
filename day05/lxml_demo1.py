from lxml import etree

'''
html文档解析方法
'''

text = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a><li>
        <li class="item-1"><a href="link2.html">second item</a><li>
        <li class="item-inactive"><a href="link3.html">third item</a><li>
        <li class="item-1"><a href="link4.html">fourth item</a><li>
        <li class="item-0"><a href="link5.html">fifth item</a><li>
    </ul>
</div>
"""
'''
lxml的使用方法
将xml或者html解析成element对象
使用的html方式进行解析的，将来解析的内容就是html文档。
如果内容没有html标签，就会自动补全
'''
html = etree.HTML(text)
# print(html)
# <Element html at 0x1d92c902bc8>
# 返回值是一个element对象

# 将element对象编程字符串
# print(etree.tostring(html,pretty_print=True))
# prtty_print = true 是指将严格按照xml格式进行输出，将会补全相应的标签
'''
<html>  
    <body><div>
        <ul>        
            <li class="item-0"><a href="link1.html">first item</a></li><li>        
            </li><li class="item-1"><a href="link2.html">second item</a></li><li>       
            </li><li class="item-inactive"><a href="link3.html">third item</a></li><li> 
            </li><li class="item-1"><a href="link4.html">fourth item</a></li><li>      
            </li><li class="item-0"><a href="link5.html">fifth item</a></li><li>
        </li></ul>
    </div></body>
</html>
'''
#1、element对象有xpath方法，可以写xpath语法进行筛选数据。
#2、元素和标签:xpath表达式最后一个内容如果是元素或者标签，将来取到的内容就是这个标签的element对象，
# 这个对象可以继续使用xpath进行选取
#3、xpath方法返回的是一个list，里面存储的是筛选出来的所有内容

# ul = html.xpath('//ul')
# [<Element ul at 0x1b2facc9388>]
ul = html.xpath('//ul')[0]
# <Element ul at 0x121749fc1c8>
# print(ul)
# 选取ul标签下的第一个li
li_first = ul.xpath('.//li[1]')
# print(li_first)
# [<Element li at 0x140459d95c8>]
# 选取属性
li_class = html.xpath('//ul/li[1]/@class')
# print(li_class)
# ['item-0']
# 选取内容
a_text = html.xpath('//ul/li[1]/a/text()')
# print(a_text)
# ['first item']