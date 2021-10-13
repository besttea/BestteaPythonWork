'''
Author: your name
Date: 2021-10-11 03:03:12
LastEditTime: 2021-10-11 03:03:13
LastEditors: your name
Description: In User Settings Edit
FilePath: \0001\绘制樱花图3.py
'''
from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)
bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0)
left(90)
pu()
backward(300)
tree(13, 100)
done()