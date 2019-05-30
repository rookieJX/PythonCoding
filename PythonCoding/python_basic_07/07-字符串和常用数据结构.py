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



if __name__ == '__main__':
    # main()
    # main_list()
    # main_List()
    main_dict()
