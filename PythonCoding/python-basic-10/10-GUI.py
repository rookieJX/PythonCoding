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

if __name__ == '__main__':
    main()