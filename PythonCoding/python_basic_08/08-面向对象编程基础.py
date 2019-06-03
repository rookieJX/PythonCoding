# ****************************
# 初识Python-08：面向对象编程
# ****************************
from time import sleep


class Student(object):
    # __init__ 是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在学习%s。'%(self.name,course_name))

    # PEP 8 要求标识符的名字用全小写多个单词用下划线连接
    def watch_av(self):
        if self.age < 18:
            print('%s只能看《熊出没》。'%self.name)
        else:
            print('%s正在观看岛国爱情片。'%self.name)


def main():

    # 创建对象
    print('**********创建对象**********')
    stu1 = Student('Ableson',19)

    # 给对象发study消息
    print('**********给对象发study消息**********')
    stu1.study('Python-100-Days')

    # 对对象发送watch_av消息
    print('**********对对象发送watch_av消息**********')
    stu1.watch_av()


# *****************************************
# 访问可见性
# *****************************************

"""
在Python中，属性的访问有两种，也就是公开的和私有的，
如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头，
"""

class Test(object):
    def __init__(self,foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

"""
但是在python中并没有从语法上严格保证私有属性或方法的私密性，
他只是给私有的属性和方法换了一个名字来"妨碍"对他们的访问，
事实上我们可以仍然访问到他们
"""

def read_private():
    print('**********访问私有属性**********')
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


# *****************************************
# 练习1：定义一个类描述数字时钟
# *****************************************

class Clock(object):

    def __init__(self,hour=0,minute=0,second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        转动时钟
        :return:
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """
        显示时间
        :return:
        """
        return '%02d:%02d:%02d'%\
               (self._hour,self._minute,self._second)

def run_clock():
    print('**********定义一个类描述数字时钟**********')
    clock = Clock(23,59,48)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


# *****************************************
# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
# *****************************************

from math import sqrt

class Point(object):

    def __init__(self,x=0,y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y
    def move_to(self,x,y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self,dx,dy):
        """
        移动指定的增量
        :param dx: 哼坐标的增量
        :param dy: 纵坐标的增量
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self,other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)'%(str(self.x),str(self.y))

def run_point():
    print('**********定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法**********')
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    # main()
    # read_private()
    # run_clock()
    run_point()