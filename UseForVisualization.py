# -*- coding: utf-8 -*-

def Arrange(table, result, d):
    ans = func(len(table)-1, d, table, result)
    print(result.items())
    print(ans)


def func(c, d, table, result):
    #c = course 的數量
    #d = 總共有的天數
    if str(c)+' '+str(d) in result:
        return result[str(c)+' '+str(d)]
    if d > c:
        value = []
        for i in range(1, d-(c-1)+1):
            value.append(func(c-1, d-i, table, result) + table[c][i])
        print(value)
        result[str(c)+' '+str(d)] = max(value)
        return result[str(c)+' '+str(d)]
    else:
        print("illegal value with corse > days")

def InitTable(table_str):
    table = []
    # Course 數量 == len(table[0])
    # Day 長度 == len(table)
    for i in range(len(table_str[0])+1):
        table.append([])
        for j in range(len(table_str)+1):
            table[i].append(float("-inf"))
    for i in range(len(table_str[0])):
        for j in range(len(table_str)):
            table[i+1][j+1] = int(table_str[j][i])
    #ShowTable(table)
    return table

def ShowTable(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j], ' ', end='')
        print()

line = "3 4 3 6"
while True:
    table_str = []
    #儲存 Table
    line = "6 6 4 7"
    table_str.append(line.split())
    line = "7 9 8 9"
    table_str.append(line.split())
    line = "8 11 9 10"
    table_str.append(line.split())
    table = InitTable(table_str)
    result = {}
    line = "7"
    #利用給定的 days 計算答案
    d = int(line)
    Arrange(table, result, d)
    break
