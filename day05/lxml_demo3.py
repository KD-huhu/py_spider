from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html" class = "a_class1">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive">
         <a href="link3.html" class="bold"></a>
         <span class="span_item1">span_text1</span>
      </li>
        <li class="item-1">
            test
         <a href="link4.html">fourth item<span class="span_item2">span_text2</span></a>
      </li>
        <li class="item-0">
         <a href="link5.html">fifth item</a>
    </ul>

</div>
'''

# 将html字符串转换为html(element对象)
html = etree.HTML(text)
#1. 获取所有的 <li> 标签
li_list = html.xpath('//li')
print(li_list)
# [<Element li at 0x2226c019488>, <Element li at 0x2226c0196c8>, <Element li at 0x2226c019708>, <Element li at 0x2226c019748>, <Element li at 0x2226c0197c8>]
#2. 继续获取<li> 标签的所有 class属性
for li in li_list:
    li_class = li.xpath('.//@class')    # 找当前节点下的所有class属性
    li_class1 = li.xpath('./@class')    # 找当前节点的class属性
    # print(li_class1)
'''
[<Element li at 0x253493d5608>, <Element li at 0x253493d5848>, <Element li at 0x253493d5888>, <Element li at 0x253493d58c8>, <Element li at 0x253493d5948>]
['item-0', 'a_class1']
['item-1']
['item-inactive', 'bold', 'span_item1']
['item-1', 'span_item2']
['item-0']
'''
'''
[<Element li at 0x1dde03f75c8>, <Element li at 0x1dde03f7808>, <Element li at 0x1dde03f7848>, <Element li at 0x1dde03f7888>, <Element li at 0x1dde03f7908>]
['item-0']
['item-1']
['item-inactive']
['item-1']
['item-0']
'''
li_classes = html.xpath('//ul/li/@class')
#3. 继续获取<li>标签下href 为 link1.html 的 <a> 标签
a = html.xpath('//ul/li/a[@href="link1.html"]')
# print(a)
#4. 获取<li> 标签下的所有 <span> 标签（包括孙子span）
span = html.xpath('//ul/li/span')
#5. 获取 <li> 标签下的<a>标签里的所有 class
a_class = html.xpath('//ul/li/a/@class')
#6. 获取最后一个 <li> 的 <a> 的 href
a_href_last = html.xpath('//ul/li[last()]/a/@href')
#7. 获取倒数第二个元素的内容
result = html.xpath('//*[last()-1]')
#8. 获取 class 值为 bold 的标签名
result1 = html.xpath('//*[]@class="bold"')[0]
