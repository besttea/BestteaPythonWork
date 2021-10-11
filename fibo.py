'''
Author: your name
Date: 2021-10-12 02:51:57
LastEditTime: 2021-10-12 02:51:58
LastEditors: your name
Description: In User Settings Edit
FilePath: \0001\fibo.py
'''
# 斐波那契(fibonacci)数列模块
 
def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result