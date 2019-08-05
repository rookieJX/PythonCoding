''''''
# from sklearn.preprocessing import label

'''
基于tkinter模块的GUI开发

GUI是图形用户界面的缩写，Python默认的GUI开发模块时tkinter。
此模块是基于Tk的，Tk是一个工具包，最初是为Tcl设计的，后来被一直到很多其他的脚本语言中，
它提供了跨平台的GUI控件。
事实上GUI开发中tkinter功能并不是很强大，开发GUI也并不是Python最擅长的工作，
如果需要使用Python开发GUI应用，wxPython、PyQt、PyGTK都是很好的选择。

'''

'''
基本上使用tkniter开发GUI应用需要以下5个步骤：

1.导入tkinter模块中我们需要的东西
2.创建一个顶层窗口对象并用它来承载整个GUI应用
3.在顶层窗口对象上添加GUI组件
4.通过代码将这些GUI组件的功能组织起来
5.进入主时间循环(main loop)
'''

import tkinter
import tkinter.messagebox

def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        float = not flag
        color,msg = ('blue','Hello,World!')\
            if flag else ('black','Goodbye,world!')
        label.config(text=msg,fg=color)


    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出么？'):
            top.quit()



    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('4000x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top,text='Hello, world!',font='AArial -32',fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过 command参数绑定时间回调函数
    button1 = tkinter.Button(panel,text='修改',command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='退出',command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主时间循环
    tkinter.mainloop()



'''
使用Pygame进行游戏开发
Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，
其中包含对图像、声音、视频、事件、碰撞等的支持。
Pygame建立在SDL的基础上。SDL是一套跨平台的多媒体开发库，用C语言实现。
'''


import pygame

# 制作游戏窗口
def game_screen_main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800,600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    #开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


# 在窗口中绘图
def game_drwan_main():
    # 初始化
    pygame.init()
    # 尺寸
    screen = pygame.display.set_mode((800,600))
    # 设置标题
    pygame.display.set_caption('大球吃小球')
    screen.fill((242,242,242))
    pygame.draw.circle(screen,(255,0,145),(100,100),30,0)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# 加载图像
def game_image_main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('----')
    screen.fill((255,120,230))
    ball_iamge = pygame.image.load('./res/ball.png')
    screen.blit(ball_iamge,(50,50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# 加载动画
def game_animate_main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('---')
    x,y = 50,50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((234,123,120))
        pygame.draw.circle(screen,(255,0,0),(x,y),30,0)
        pygame.display.flip()
        pygame.time.delay(3)
        x,y = x+5,y+5

# 碰撞检测
from enum import Enum,unique
from math import sqrt
from random import randint

@unique
class Color(Enum):
    '''颜色'''

    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GRAY = (242,242,242)

    @staticmethod
    def random_color():
        '''获得随机颜色'''
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)


class Ball(object):
    '''球'''

    def __init__(self,x,y,radius,sx,sy,color=Color.RED):
        '''初始化方法'''
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self,screen):
        '''移动'''
        self.x += self.sx
        self.y += self.sy

        if self.x - self.radius <= 0 or \
            self.x + self.radius >= screen.get_width():
            self.sx = -self.sx

        if self.y - self.radius <= 0 or \
            self.y + self.radius >= screen.get_height():
            self.sy = - self.sy

    def eat(self,other):
        '''吃其他球'''

        if self.alive and other.alive and self != other:
            dx,dy = self.x - other.x,self.y - other.y
            distance = sqrt(dx ** 2 + dy **2)
            if distance < self.radius + other.radius \
                and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self,screen):
        '''在窗口上绘制球'''
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)


def game_event_main():

    balls = []
    pygame.init()
    screen = pygame.display.set_mode((1600, 1200))
    pygame.display.set_caption('大球游戏')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                radius = randint(1,10)
                sx,sy = randint(-10,10),randint(-10,10)
                color = Color.random_color()
                ball = Ball(x,y,radius,sx,sy,color)
                balls.append(ball)
        screen.fill((255,255,255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()
        pygame.time.delay(1)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    # main()
    # game_screen_main()
    # game_drwan_main()
    # game_image_main()
    # game_animate_main()
    game_event_main()