# ****************************
# 初识Python-06：函数和模块的使用
# ****************************


""""""

"""
如果我们导入的模块除了定义函数之外还有可以执行代码，
那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们并不希望如此，因此如果我们在模块中编写了执行代码，
最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行模块，if条件下的代码是不会执行的，
因为只有直接执行的模块的名字才是 '__main__'
"""

def foo():
    print('This is foo_test_03 function foo()')

def bar():
    print('This is foo_test_03 function bar()')

# __name__ 是Python中一个隐含的变量，他嗲表了模块的名字
# 只有Python解释器直接执行的模块的名字才是 __main__

if __name__ == '__main__':
    print('call foo_test_03 foo()')
    foo()
    print('call foo_test_03 bar()')
    bar()