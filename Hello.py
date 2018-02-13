import os
import requests
import sys
import math

# print("hello baijy")
# print(os.getcwd())
# print(os.getcwd())

### pip的使用方法以及requests模块的使用
# r = requests.get("http://www.baidu.com")
# print(r.content)

### 字符串的使用方法
# print("我是双引号的")
# print('我是单引号的')
# print('''我是
# 三引号的''')

# name = '白建业'
# age = '''34'''
# age2 = 34
# print("我叫{0},我的年龄是{1}".format(name, age))
# print("我叫"+name+"\n我的年龄是"+str(age2))


### 数字使用方法
# a = 3
# b = 3.5
# c = complex(3, 5)
# print("real:{0},imag:{1}".format(c.real, c.imag))

# i = 2
# print("int:{0},float:{1}".format(i, float(i)))
# print("i is type of {0},float(i) is type of {1}".format(type(i), type(float(i))))

# a = 3
# b = 17
# print("result:{0}".format(b / a))
# print("result:{0}".format(b // a))
# print("result:{0}".format(b % a))
# print(sys.float_info)



### list的使用方法
# list = [1, 2.4, 'woshi', complex(4, 5.9)]
# print("list is :" + str(list))
# print("the first element is {0}".format(list[0]))
# list[3] = 99
# print("changed list is " + str(list))
# list.append(88)
# print("changed list is " + str(list))
# list.remove(99)
# print("changed list is " + str(list))
# del list[0]
# print("changed list is " + str(list))
# print("woshi 是否在List中：" + str('woshi' in list))
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# print("list 合并后的结果为：" + str(a + b))
# print("list 的长度为：" + str(len(a)))
# print("自动生成7个haha的列表：" + str(['haha'] * 7))

# list = [1, 2, 3, 4, 5, 6, 7]
# print("list[1]:" + str(list[1]))
# print("list[-1]:" + str(list[-1]))
# print("list[1:]:" + str(list[1:]))
# print("list[-3:-1]:" + str(list[-3:-1]))
# print("list[1:5]" + str(list[1:5]))

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# # print("cmp(a,b)" + str(cmp(a, b)))
# print("len(a):" + str(len(a)))
# print("max(a):" + str(max(a)))
# print("min(a):" + str(min(a)))
# l = [1, 3, 5, 7, 3, 2, 3, 4, 5, 6, 7, 5, 4, 3, 4, 5, 6, 7, 0]
# print("l:" + str(l))
# l.append(7)
# print("l.append(7):" + str(l))
# l.remove(3)
# print("l.remove(3)" + str(l))
# l.pop()
# print("l.pop()" + str(l))
# print("l.index(3)" + str(l.index(3)))
# l.sort()
# print("l.sort()" + str(l))
# l.reverse()
# print("l.reverse()" + str(l))
# print("l.count(5)" + str(l.count(5)))
# l.insert(4, 99)
# print("l.insert(4,99):" + str(l))
# ex = ['a', 'b', 'c']
# l.extend(ex)
# print("l.extend(ex):" + str(l))

### 元组的使用
# mix_tuple = (1, 4.5, 'ad', complex(3, 5.6))
# print("mix_tuple[3]:" + str(mix_tuple[3]))
# del mix_tuple
# print('del tuple:'+ str(mix_tuple))
# t = (1, 3, 5, 7, 3, 2, 3, 4, 5, 6, 7, 5, 4, 3, 4, 5, 6, 7, 0)
# print("t:" + str(t))
# print('len(t):' + str(len(t)))
# print("t.count(3)" + str(t.count(3)))
# print("t.index(3)" + str(t.index(3)))
# print("max(t)" + str(max(t)))
# print("min(t)" + str(min(t)))
# ex = ('a', 'b')
# print("t+ex:" + str(t + ex))
# item = ('haha')
# print("(haha)*4:" + str(item * 4))
# print("is 3 in t:"+str(3 in t))
# lt = (0,1,2,3,4,5,6,7,8)
# print("lt:"+str(lt))
# print("lt[3]:"+str(lt[3]))
# print("lt[-1]:"+str(lt[-1]))
# print("lt[3:5]:"+str(lt[3:5]))
# print("lt[-5:-3]:"+str(lt[-5:-3]))
# print("lt[-5:]:"+str(lt[-5:]))
# print("lt[:-3]:"+str(lt[:-3]))

### 字典的使用（注意：可以用处理列表和字典以外的任何数据类型充当键，包括tuple。因为List和字典是可变的，而tuple是不可变的）
# d = {"k1": 1, "k2": 2, 3: "k3", "k4": "k4", 5: 5}
# print("d[k1]:" + str(d["k1"]))
# print("d:" + str(d))
# d[5] = 6
# print("d[5] = 6:" + str(d))
# d["add"] = 7.0
# print('d["add"]=7.0:' + str(d))
# del d["add"]
# print('del d["add"]:' + str(d))
# # print('d.clear():' + str(d.clear()))
# ds = {"sdsfsfd": 234, "sdfgfdf": 89}
# print("ds.copy()" + str(ds.copy()))
# dd = {{"a": 1}: 4}
# print("dd is :" + str(dd))

### 函数的使用
# def say():
#     print("hello world")
#
#
# say()
#
#
# def plus(a=0, b=1, c=0):
#     return a + b + c
#
#
# print(str(plus(3)))
# print(str(plus()))
# print(str(plus(11, c=1)))
# print(str(plus(3, 5)))
# print(str(plus(c=2, b=2, a=1)))


# def paramSample(arg1, *arg2, **arg3):
#     print("arg1:{0};arg2:{1};arg3:{2}".format(arg1, arg2, arg3))
#
#
# paramSample("arg1", 1, 2, 3, 4, 5, 6, k1=1, k2=2, k3=3)

### 全局变量和局部变量
# x = 60
#
#
# def aa():
#     x = 4
#     print("x:" + str(x))
#
#
# aa()
# print("x:" + str(x))
#
# y = 60
#
#
# def bb():
#     global y
#     y = 5
#     print("y:" + str(y))
#
#
# bb()
# print("y:" + str(y))


### 控制语句(if)
# arg = int(input("please input:"))
# if arg > 0:
#     print("我是正数")
# elif arg < 0:
#     print("我是负数")
# else:
#     print("我是零")


### for语句的用法
# for i in range(1, 10):
#     print(i)
# else:
#     print("for is done")
#
# for i in [1, 3, 5, 7, 9]:
#     print(i)
#
# for i in (2, 4, 6, 8, 0):
#     print(i)

# dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 4}
# for i in dict:
#     print("key:{0}&value:{1}".format(i, dict[i]))
#
# for key, value in dict.items():
#     print("key:{0}&value:{1}".format(key, value))


### while语句的用法
# result = 45
# flag = False
#
# while not flag:
#     inputs = int(input("guess:"))
#     if inputs == result:
#         flag = True
#         print("success!!!!")


### continue 和 pass 的区别
# l = [0,1,2]
# print("use continue")
# for i in l:
#     if not i:
#         continue
#     print(i)
# print("use pass")
# for i in l:
#     if not i:
#         pass
#         print("after pass")
#     print(i)


### 文件的读写操作
# str = '''我是白建业
# 我工作了相当长的时间
#
#
#
# 我对此有些厌烦了'''
#
# f = open("testfile.txt","w")
# f.write(str)
# f.close()
#
# r = open("testfile.txt")
#
# while True:
#     s = r.readline()
#     if len(s) == 0:
#         break
#     print(s)
# f.close()


### 异常处理
# while True:
#     try:
#         i = int(input("please input:"))
#         break
#     except ValueError:
#         print("input again")
#
# try:
#     f = open("test.txt")
#     while True:
#         s = f.readline()
#         if len(s) == 0:
#             break
#         i = int(s.strip())
#         print(i)
# except OSError as ose:
#     print("--->" + str(ose))
# except ValueError:
#     print("value error")
# finally:
#     f.close()


### 面向对象编程
# class student:
#     def __init__(self, name='noname', age=0):
#         self.name = name
#         self.age = age
#
#     def intro(self):
#         print("My name is {0},I'am {1} years old.".format(self.name, self.age))
#
#
# s = student("baijianye", 34)
# s.intro()


###函数装饰器
# def candle(func):
#     def insert():
#         return "i insert a candle on " + func()
#
#     return insert
#
#
# @candle
# def make():
#     return "cake"
#
#
# print(str(make()))



### 图形编程
# from tkinter import *
# import tkinter.simpledialog as dl
# import tkinter.messagebox as ms
#
# root = Tk()
# l = Label(root, text="welcome")
# l.pack()
#
# ms.showinfo("title1", "please input your name")
# name = dl.askstring("String","input a string")
# ms.showinfo("sayhi", "hello " + name)


### Web编程
import web
urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World!"
        return greeting
if __name__ == "__main__":
    app.run()
