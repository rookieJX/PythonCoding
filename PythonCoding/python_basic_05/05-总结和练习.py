# ****************************
# 初识Python-05 ： 总结和练习
# ****************************


""""""
# ****************************
# 练习1：寻找水仙花数
# ****************************


"""
寻找水仙花数

152/100 = 1.52
152 // 100 = 1

Version：0.1
Author：Ableson
"""

print('**********寻找水仙花数**********')

for i in range(100,1000):
    if(((i%10)**3 + (i%100//10)**3 + (i//100)**3) == i):
        print('%d'%(i))


"""
寻找完美数
第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6

Version：0.1
Author：Ableson
"""

print('**********寻找完美数**********')
for i in range(1,1000):
    sum = 0
    for j in range(1,int(i/2+1)):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)



"""
百钱买百鸡问题

Version：0.1
Author：Ableson
"""

print('**********百钱买百鸡问题**********')
for i in range(0,20):
    for j in range(1,34):
        if (i * 5 + j * 3 + (100-i-j)/3) == 100:
            print('公鸡:%d,母鸡:%d,小鸡:%d'%(i,j,100-i-j))

"""
生成斐波拉契数列

Version：0.1
Author：Ableson
"""

print('**********生成斐波拉契数列**********')
def fib(n):
    a,b = 1,1
    while a < n:
        print(a,end=' ')
        a,b = b , a+b
fib(100)
