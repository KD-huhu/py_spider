# 父类
class A:
    def __init__(self):
        print('父类init被触发')

    def run(self):
        print('父类的run被调用')

# 子类
class B(A):
    def __init__(self):
        print('子类init被调用')

    def run(self):
        print('子类的run被调用')

# 实例化过程
B()
# 子类init被调用
# 实例化的时候，会调用__init__方法

B().run()
'''
子类init被调用
子类的run被调用
'''
# 会先再次实例化，之后再执行run方法
