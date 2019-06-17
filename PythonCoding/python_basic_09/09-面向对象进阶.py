##
# 面向对象进阶
# #
''''''

###
# @property装饰器
# ##

"""
python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
但是有些直接暴露到外界也是有问题的。
之前建议将属性命名以下划线开头，通过这种方式按时属性是受保护的，
如果想访问可以通过属性的getter和setter方法进行属性的操作。
可以使用@property包装器来包装getter和setter方法
"""

# 使用@property装饰器
class Person(object):



    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter 方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self,age):
        self._age = age

    # 修改器 - setter 方法
    @name.setter
    def name(self,name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.'%(self._name))
        else:
            print('%s正在玩斗地主.'%(self._name))


def use_person():
    print('**********使用@property装饰器**********')
    person = Person('Ableson',10)
    person.play()
    person.age = 30
    person.play()
    person.name = 'ABLESON'
    person.play()


# __slots__魔法
'''
Python是一门动态语言。
通常，动态语言允许我们在程序运行时给对象绑定新的属性或者方法
也可以对已绑定的属性和方法进行解绑定。
但是如果我们需要限定自定义类型的对象只能绑定某些属性
可以通过在类中定义 __slots__ 变量来进行限定。
需要主义的是 __slots__的限定只对当前的类的对象生效，对子类并不起任何作用
'''

class slots_person(object):



    # 限定slots_person对象只能绑定_name,_age和_gender属性
    __slots__ = ('_name','_age','_gender')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % (self._name))
        else:
            print('%s正在玩斗地主.' % (self._name))

def use_slots_person():
    print('**********使用__slots__**********')
    person = slots_person('Ableson',12)
    person.play()
    person._gender = '男'
    # AttributeError: 'slots_person' object has no attribute '_is_gay'
    # person._is_gay = True



##
# 静态方法和类方法
# ##
'''
之前我们定义的都是对象方法，也就是这些方法都是发送给对象的消息。
事实上并不是所有的需求都需要我们创建对象方法
'''

from math import sqrt

class Triangle(object):

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a+b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

'''
和静态方法类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls
它代表的是当前类相关的信息的对象
'''

from time import time,localtime,sleep

class Clock(object):
    # 数字时钟
    def __init__(self,hour=0,minute=0,second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def run(self):
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
        return '%02d:%02d:%02d'%(self._hour,self._minute,self._second)

def use_clock():
    print('**********类方法**********')
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

def use_triangle():
    print('**********静态方法和类方法**********')

    a,b,c = 3,4,5
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())

if __name__ == '__main__':
    # use_person()
    # use_slots_person()
    # use_triangle()
    use_clock()