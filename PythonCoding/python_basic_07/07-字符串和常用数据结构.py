# ****************************
# 初识Python-07：字符串和常用数据结构
# ****************************

""""""


# ****************************
# 使用字符串
# ****************************

def main():

    str1 = 'hello world!'

    # 通过len函数计算字符串的长度
    print('**********通过len函数计算字符串的长度**********')
    print(len(str1))

    # 获得字符串首字母大写的拷贝
    print('**********获得字符串首字母大写的拷贝**********')
    print(str1.capitalize())

    # 获得字符串变大写后的拷贝
    print('***********获得字符串变大写后的拷贝**********')
    print(str1.upper())

    # 从字符串中查找子串所在位置
    print('**********从字符串中查找子串所在位置**********')
    print(str1.find('or'))
    print(str1.find('shit'))

    # 与find类似，但是找不到子串会报错
    print('**********与find类似，但是找不到子串会报错**********')
    print(str1.index('or'))
    print(str1.index('lo'))

    # 检查字符串是否已制定的字符串开头
    print('**********检查字符串是否已制定的字符串开头**********')
    print(str1.startswith('He'))
    print(str1.startswith('hel'))

    # 检查字符串是否已制定的字符串结尾
    print('**********检查字符串是否已制定的字符串结尾**********')
    print(str1.endswith('!'))

    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print('**********将字符串以指定的宽度居中并在两侧填充指定的字符**********')
    print(str1.center(50,'-'))

    # 将字符串以指定的宽度靠右防止左侧填充指定的字符
    print('**********将字符串以指定的宽度靠右防止左侧填充指定的字符**********')
    print(str1.rjust(50,'-'))

    # 从字符串中取出指定位置的字符（下标运算）
    str2 = 'abc123456'
    print('**********从字符串中取出指定位置的字符（下标运算）**********')
    print(str2[2])

    # 字符串切片（从指定的开始索引到指定的结束索引）
    print('**********字符串切片（从指定的开始索引到指定的结束索引）**********')
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])
    print(str2[-3:-1])

    # 检查字符串是否由数字构成
    print('**********检查字符串是否由数字构成**********')
    print(str2.isdigit())

    # 检查字符串是否以字母构成
    print('**********检查字符串是否以字母构成**********')
    print(str2.isalpha())

    # 检查字符串是否以数字和字母构成
    print('**********检查字符串是否以数字和字母构成**********')
    print(str2.isalnum())

    # 获得字符串修剪左右两侧空格的拷贝
    str3 = '   gkhlj.asolj '
    print('**********获得字符串修剪左右两侧空格的拷贝**********')
    print(str3.strip())




# ****************************
# 使用列表
# ****************************
import sys

def main_list():
    print('**********使用列表**********')

    list1 = [1,3,5,7,100]

    # 打印列表
    print('**********打印列表**********')
    print(list1)

    # 添加多个相同元素
    print('**********添加多个相同元素**********')
    list2 = ['hello'] * 5
    print(list2)

    # 计算列表长度（元素个数）
    print('**********计算列表长度（元素个数）**********')
    print(len(list1))

    # 下标（索引）运算
    print('**********下标（索引）运算**********')
    print(list1[0])
    print(list1[-1])
    print(list1[-3])

    # 改变列表中指定下标元素
    print('**********改变列表中指定下标元素**********')
    list1[2] = 1000
    print(list1)

    # 添加元素
    print('**********添加元素**********')
    list1.append(123456)
    print(list1)
    list1.insert(1 ,20)
    print(list1)
    list1 += [1000,200]
    print(list1)

    # 删除元素
    print('**********删除元素**********')
    list1.remove(3)
    print(list1)

    if 1234 in list1:
        list1.remove(1234)
    print(list1)

    del list1[0]
    print(list1)

    # 清空列表
    print('**********清空列表**********')
    list1.clear()
    print(list1)

    # 列表做切片操作
    print('**********列表做切片操作**********')
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 循环遍历列表元素
    print('**********循环遍历列表元素**********')
    for fruit in fruits:
        print(fruit.title(),end=' ')
    print()

    # 列表切片
    print('**********列表切片**********')
    fruits2 = fruits[1:4]
    print(fruits2)

    # 创建新的列表引用
    print('**********创建新的列表引用**********')
    fruits3 = fruits # 没有复制新的列表，只是创建了新的引用
    print(fruits3)

    # 通过完整的切片操作来复制列表
    print('**********通过完整的切片操作来复制列表**********')
    fruits4 = fruits[:]
    print(fruits4)

    # 通过反向切片操作来获得翻转后的列表的拷贝
    print('**********通过反向切片操作来获得翻转后的列表的拷贝**********')
    fruits5 = fruits[::-1]
    print(fruits5)


    # 对列表排序操作
    print('**********对列表排序操作**********')
    rever_list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    rever_list2 = sorted(rever_list1) # sorted函数返回列表排序后的拷贝不会修改传入的列表
    print(rever_list1)
    print(rever_list2)
    rever_list3 = sorted(rever_list1,reverse=True)
    print(rever_list3)

    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母排序
    print('**********通过key关键字参数指定根据字符串长度进行排序而不是默认的字母排序**********')
    rever_list4 = sorted(rever_list1,key=len)
    print(rever_list4)

    # 给列表对象发出排序消息直接在列表对象上进行排序
    print('**********给列表对象发出排序消息直接在列表对象上进行排序**********')
    rever_list1.sort(reverse=True)
    print(rever_list1)


    # 通过列表的生成式语法来创建列表
    print('**********通过列表的生成式语法来创建列表**********')
    f = [x for  x in range(1,10)]
    print(f)
    f = [x + y for x in  'ABCD' for y in  '123456']
    print(f)

    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪，所以需要耗费较多的内存空间
    print('**********用列表的生成表达式语法创建列表容器用这种语法创建列表之后元素已经准备就绪，所以需要耗费较多的内存空间**********')
    f = [x ** 2 for x in range(1,1000)]
    print(sys.getsizeof(f)) # 查看对象占用内存的字节数
    print(f)

    # 请注意下面代码创建的不是一个列表而是一个生成器对象
    # 通过生成器对象可以获取到数据但他不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据（需要额外的花费时间）
    print('**********创建生成器对象**********')
    f = (x ** 2 for x in  range(1,1000))
    print(sys.getsizeof(f)) # 相比生成时生成器不占用存储的空间
    print(f)



# ****************************
# 使用元组
# ****************************

def main_List():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print('**********定义元组**********')
    print(t)

    # 获取元组中元素
    print('**********获取元组中元素**********')
    print(t[0])

    # 遍历元组中的值
    print('**********遍历元组中的值**********')
    for member in t:
        print(member)

    # 重新给元组赋值
    print('**********重新给元组赋值**********')
    # t[0] = 'Ableson'
    print('会报错')

    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    print('**********变量t重新引用了新的元组原来的元组将被垃圾回收**********')
    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    # 将元组转换成列表
    print('**********将元组转换成列表**********')
    person = list(t)
    print(person)

    # 列表是可修改元素的
    print('**********列表是可修改元素的**********')
    person[0] = 'Ableson'
    print(person)

    # 将列表转换为元组
    print('**********将列表转换为元组**********')
    fruit_list = ['apple','banana','orange']
    fruit_tuple = tuple(fruit_list)
    print(fruit_tuple)


# ****************************
# 使用集合
# ****************************

def main_dict():
    # 定义集合
    set1 = {1,2,3,4,5,5,6,5}
    print('**********定义集合**********')
    print(set1)

    # 集合元素个数
    print('**********集合元素个数**********')
    print(len(set1))

    # 快速创建集合
    print('**********快速创建集合**********')
    set2 = set(range(1,10))
    print(set2)

    # 集合中添加元素
    print('**********集合中添加元素**********')
    set1.add(100)
    set1.add(1)
    print(set1)

    # 更新集合
    print('**********更新集合**********')
    set2.update([11,12])
    print(set2)

    # remove的元素如果不存在会引发KeyError
    print('**********remove的元素如果不存在会引发KeyError**********')
    set1.remove(1)
    print(set1)


    # 遍历集合容器
    print('**********遍历集合容器**********')
    for elem in set2:
        print(elem,end=' ')
    print()


    # 将元组转换成集合
    print('**********将元组转换成集合**********')
    set3 = set((1,2,3,3,2,1))
    print(set3)

    # 删除第一个元素
    print('**********删除第一个元素**********')
    print(set3.pop())

    # 集合的交集
    print('**********集合的交集**********')
    print('set1 = ',set1)
    print('set2 = ',set2)
    print(set1 & set2)
    print(set1.intersection(set2))

    # 集合的并集
    print('**********集合的并集**********')
    print('set1 = ',set1)
    print('set2 = ',set2)
    print(set1 | set2)
    print(set1.union(set2))

    # 集合的差集
    print('**********集合的差集**********')
    print('set1 = ', set1)
    print('set2 = ', set2)
    print(set1 - set2)
    print(set1.difference(set2))

    # 集合对称差
    print('**********集合对称差**********')
    print('set1 = ', set1)
    print('set2 = ', set2)
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))

    # 判断子集
    print('**********判断子集**********')
    print(set2 <= set1)
    print(set2.issubset(set1))

    # 判断超集
    print('**********判断超集**********')
    print(set1 >= set2)
    print(set1.issuperset(set2))


# ****************************
# 使用字典
# ****************************

def main_dictionary():

    # 创建字典
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print('**********创建字典**********')
    print(scores)

    # 通过键获取字典中的值
    print('**********通过键获取字典中的值**********')
    print(scores['狄仁杰'])

    # 对字典进行遍历
    print('**********对字典进行遍历**********')
    for elem in scores:
        print('%s\t--->\t%d'%(elem,scores[elem]))

    # 更新字典中的元素
    print('**********更新字典中的元素**********')
    scores['狄仁杰'] = 1000
    print(scores)

    # 更新字典添加元素
    print('**********更新字典添加元素**********')
    scores.update(王大爷=190,李分=9009)
    print(scores)

    # get方法也是通过键获取对应的值，但是可以设置默认值
    print('***********get方法也是通过键获取对应的值，但是可以设置默认值***********')
    print(scores.get('武则天',60))

    # 删除字典中的元素
    print('***********删除字典中的元素***********')
    print(scores.popitem())
    print(scores)
    print(scores.pop('狄仁杰'))
    print(scores)

    # 清空字典
    print('***********清空字典**********')
    scores.clear()
    print(scores)



# ****************************
# 练习
# ****************************

"""
练习1：在屏幕上显示跑马灯文字
"""

import os
import time

def main_lianxi_01():
    content = '北京欢迎你为你开天辟地…………'
    print('**********在屏幕上显示跑马灯文字**********')
    while True:
        # 清理屏幕上的输出
        os.system("clear")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
"""

import random
def generate_code(code_len = 4):
    print('**********设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成**********')
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

"""
练习3：设计一个函数返回给定文件名的后缀名
"""

def get_suffix(filename,has_dot=False):
    """
    获取文件后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    print('**********设计一个函数返回给定文件名的后缀名**********')
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos+1
        return filename[index:]
    else:
        return ''
"""
练习4：设计一个函数返回传入的列表中最大的和第二大的元素的值
"""

def get_max2(x):
    print('**********设计一个函数返回传入的列表中最大的和第二大的元素的值**********')
    m1,m2 = (x[0],x[1]) if (x[0] > x[1]) else (x[1],x[0])
    for index in range(2,len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2

"""
练习5：计算指定的年月日是这一年的第几天
"""
def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,date):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    print('**********计算指定的年月日是这一年的第几天**********')
    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total + date

"""
练习6：打印杨辉三角
"""

def main_lianxi_06():
    print('**********打印杨辉三角**********')
    num = int(input('Number of rows: '))
    yh = [[]] * num
    print(yh)
    print([None] * num)
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col],end='\t')
        print()

# ****************************
# 综合案例
# ****************************

"""
综合案例1：双色球选号
"""

from random import randrange,randint,sample

def display(balls):
    """
    输入列表中的双色球号码
    :param balls: 双色球
    :return:
    """

    for index,ball in enumerate(balls):
        if index == len((balls)) - 1:
            print('|',end='')
        print('%02d\t'%ball,end='')
    print()

def random_select():
    """
    随机选择一组号码
    :return:
    """
    red_balls = [x for x in  range(1,34)]
    selected_balls = []
    selected_balls = sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def main_zonghe_01():
    print('**********双色球选号**********')
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    # main()
    # main_list()
    # main_List()
    # main_dict()
    # main_dictionary()
    # main_lianxi_01()
    # print(generate_code(30))
    # print(get_max2((1,2,3,4,5,6,7,8,9))
    # print(which_day(2001,12,3))
    # main_lianxi_06()
    main_zonghe_01()