# ****************************
# 初识Python-06：函数和模块的使用
# ****************************


""""""

# ****************************
# 函数的作用
# ****************************

"""
函数的作用是减少重复
在Python中，可以使用 def 定义函数
"""


# ****************************
# 函数的参数
# ****************************

"""
在Python中，函数的参数可以有默认值，也支持使用可变参数。
"""

"""
举例说明：摇骰子
"""

print('**********摇骰子**********')

from  random import randint

def rolll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return  total

print(rolll_dice(10))

"""
举例说明：可变参数
"""

print('**********可变参数**********')

def add(a = 0,b = 0, c = 0):
    return  a + b + c

print(add())
print(add(b = 10,a = 100,))

"""
举例说明：我们可能通过多个参数进行计算，参数的数量由调用者来决定。在不确定参数个数的时候，我们可以使用可变参数
"""

print('**********不确定参数个数的可变参数**********')
def add_args(*args):
    total = 0
    for var in args:
        total += var
    return total

print(add_args(10,1,1,2,1,3,124,1,4,1,41,241,4,1,4,124,12))


# ****************************
# 用模块管理函数
# ****************************

"""
对于任何编程语言来说，变量、函数命名都是比较麻烦的事情，可能会遇到命名冲突的问题。最简单的场景是在 .py文件中定义两个同名的函数
由于Python没有函数重载的概念，那么后面定义的命名就会覆盖之前的定义。
也就是说定义两个，实际上只有一个是存在的。
"""

"""
举例说明：验证函数命名无重载概念，只会覆盖
"""

print('**********验证函数命名无重载概念，只会覆盖**********')

def foo():
    print('hello first foo()')

def foo():
    print('hello second foo()')

foo()

"""
解决命名冲突，不同的 .py文件中可以有相同的命名
"""

"""
举例说明：解决命名冲突
"""

print('**********解决命名冲突**********')

import python_basic_06.foo_test_01 as foo_01
import python_basic_06.foo_test_02 as foo_02
foo_01.foo()
foo_02.foo()

# ****************************
# 函数 __mian__ 和 __name__
# ****************************

import python_basic_06.foo_test_03 as foo_03

# 在foo_test_03 中，我们定义了一系列可执行代码，这里引入并不会执行


# ****************************
# 练习1：实现计算求最大公约数和最小公倍数的函数
# ****************************

"""
实现计算求最大公约数和最小公倍数的函数
"""

print('**********实现计算求最大公约数和最小公倍数的函数**********')
def gcd(x,y):
    (x,y) = (y,x) if x > y else (x,y)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x,y):
    return x * y // gcd(x,y)


# ****************************
# 练习2：实现判断一个数是不是回文数的函数
# ****************************

print('**********实现判断一个数是不是回文数的函数**********')
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return  total == num


# ****************************
# 练习3：实现判断一个数是不是素数的函数
# ****************************

print('**********实现判断一个数是不是素数的函数**********')
def is_prime(num):
    for factor in range(2,int(num/2+1)):
        if num % factor == 0:
            return False
    return True if num != 1 else False

print(is_prime(4))

# ****************************
# 练习4：写一个程序判断输入的正整数是不是回文素数
# ****************************

print('**********写一个程序判断输入的正整数是不是回文素数**********')
if __name__ == '__main__':
    num = int(input('请输入正整数:'))
    if is_prime(num) and is_palindrome(num):
        print('%d是回文素数'%num)
    else:
        print('%d不是回文素数'%num)



# ****************************
# Python中 有关变量作用于的问题
# ****************************
