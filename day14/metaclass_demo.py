def a():
    print('in func a!')

# print(type(a))
# print(a.__class__)
# <class 'function'>
# <class 'function'>

class Foo:
    pass

# print(Foo)
# print(Foo())
# <class '__main__.Foo'>
# <__main__.Foo object at 0x0000024B21A8E308> 已经进行实例化，对应为实例化ID

# Foo = type('Foo',(),{})
# Foo.a = a
# print(Foo.a)
# <function a at 0x00000229C1F860D8>
# print(Foo.a())
# in func a!  调用Foo中的a函数
# None        调用后的返回值为空

f = Foo()
# print(dir(f))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
f对应的所有方法
'''

b = 123
# print(b.__class__)
# <class 'int'>
# print(b.__class__.__class__)
# <class 'type'>

# 当一个类实例化的时候：Foo()
# __new__：---初始化这个类---
# __init__:---初始化这个对象
