# ****************************
# 初识Python03 分支结构
# ****************************

""""""

# ****************************
# if语句的使用
# ****************************


"""
用户身份验证

Version：0.1
Author：Ableson
"""

print('**********用户身份验证**********')
username = input('请输入用户名：')
password = input('请输入口令：')
# 如果希望输入用户口令是，终端没有回显，可以使用getpass模块的getpass函数
# import getpass
# password = getpass.fallback_getpass('请输入用户口令：')
if username == 'admin' and password == '123':
    print('用户身份验证成功')
else:
    print('用户身份验证失败')



"""
分段函数求值


        3x - 5 (x > 1)
f(x) =  x + 2  (-1 <= x <= 1)
        5x + 3 (x < -1)
        
Version：0.1
Author：Ableson
"""
print('**********分段函数求值**********')
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f'%(x,y))


# ****************************
# 练习1：英制单位与公制单位互换
# ****************************

"""
英制单位英寸和公制单位厘米互换

Version：0.1
Author：Ableson
"""
print('**********英制单位与公制单位互换**********')
value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米'%(value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸'%(value,value/2.54))
else:
    print('请输入有效单位')


# ****************************
# 练习2：掷骰子决定做什么
# ****************************

"""
掷骰子决定做什么

Version：0.1
Author：Ableson
"""

from random import randint

print('**********掷骰子决定做什么**********')
face = randint(1,6)
if face == 1:
    result = '唱歌'
elif face == 2:
    result = '跳舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '练绕口令'
else:
    result = '讲冷笑话'
print(result)


# ****************************
# 练习3：百分制成绩转等级制
# ****************************

"""
百分制成绩转等级制
90分以上       --> A
80分~89分      --> B 
70分~79分      --> C
60分~69分      --> D
60分以下       --> E

Version：0.1
Author：Ableson
"""

print('**********百分制成绩转等级制**********')
score = float(input('请输入成绩： '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('%.2f 对应的等级是:%s'%(score,grade))




# ****************************
# 练习4：输入三条边长如果能构成三角形就计算周长和面积
# ****************************

"""
输入三条边长如果能构成三角形就计算周长和面积

Version：0.1
Author：Ableson
"""

import math

print('**********输入三条边长如果能构成三角形就计算周长和面积**********')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('周长：%f'%(a + b + c))
    p = (a + b + c)/2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积：%f'%(area))
else:
    print('不能构成三角形')


# ****************************
# 练习5：个人所得税计算器
# ****************************

"""
个人所得税计算器

Version：0.1
Author：Ableson
"""

salary = float(input('请输入本月收入：'))
insurance = float(input('五险一金：'))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税：￥%.2f元'%(tax))
print('实际到手收入：￥%.2f元'%(diff + 3500 - tax))
