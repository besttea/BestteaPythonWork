'''
Author:zengke 
Date: 2021-09-13 10:28:51
LastEditTime: 2021-09-13 10:29:49
LastEditors: Please set LastEditors
Description : example of chapter II
FilePath: \0001\example21.py
'''
'''
4: 输入某年某月某日，判断这一天是这一年的第几天？
'''
def fun_4(year,month,day):
    sum = 0
    month_day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if((0 != year % 100 and 0 == year % 100) or (year % 400)):
        month_day[2] = 29
    if(day > month_day[month] or day < 1 or month > 12 or month < 1):
        print ("error")
        return -1
    else:
        for n in range(1,month):
            sum += month_day[n]
        sum += day
        
    return sum
        
print (fun_4(2015,6,7)) 