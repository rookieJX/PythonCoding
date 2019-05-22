# ****************************
# 初识Python04 循环结构
# ****************************

""""""
# ****************************
# for-in循环
# ****************************

"""
用 for 循环实现 1~100 求和

Version：0.1
Author：Ableson
"""

print('**********用 for 循环实现 1~100 求和**********')
sum = 0
for x in range(0,101):
    sum += x

print(sum)

"""
用 for 循环实现 1~100 之间的偶数求和

Version：0.1
Author：Ableson
"""


print('**********用 for 循环实现 1~100 之间的偶数求和**********')
sum = 0
for x in range(2,101,2):
    sum += x
print(sum)


"""
用 for 循环分支实现 1~100 之间的偶数求和

Version：0.1
Author：Ableson
"""

print('**********用 for 循环分支实现 1~100 之间的偶数求和**********')
sum = 0
for x in range(0,101):
    if x % 2 == 0:
        sum += x
print(sum)


# ****************************
# while循环
# ****************************

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version：0.1
Author：Ableson
"""

import random

print('**********猜数字游戏**********')
answer = random.randint(1,100)
print('随机答案%d'%(answer))
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！！！')
        break
    print('你一共猜了%d次'%(counter))
    if counter > 7:
        print('你的智商余额明显不足')

"""
输出乘法口诀表（九九表）

Version：0.1
Author：Ableson
"""

print('**********输出乘法口诀表（九九表）**********')
for i in  range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end='\t')
    print()


# ****************************
# 练习1：输入一个数判断是不是素数
# ****************************

"""
输入一个数判断是不是素数

Version：0.1
Author：Ableson
"""

from math import sqrt
print('**********输入一个数判断是不是素数***********')
num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2,end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数'%num)
else:
    print('%d不是素数'%num)

# ****************************
# 练习2：输入两个正整数，计算最大公约数和最小公倍数
# ****************************

"""
输入两个正整数，计算最大公约数和最小公倍数

Version：0.1
Author：Ableson
"""

print('**********输入两个正整数，计算最大公约数和最小公倍数**********')
x = int(input('x = '))
y = int(input('y = '))

if x > y :
    x,y = y,x
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d'%(x,y,factor))
        print('%d和%d的最小公倍数是%d'%(x,y,x*y//factor))
        break

# ****************************
# 练习3：打印三角形图案
# ****************************

"""
打印三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version：0.1
Author：Ableson
"""

print('**********打印三角形图案**********')

row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i + 1):
        print('*',end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ',end='')
        else:
            print('*',end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ',end='')
    for _ in range(2 * i + 1):
        print('*',end='')
    print()