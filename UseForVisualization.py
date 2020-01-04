# -*- coding: utf-8 -*-

def Arrange(table, result, d):
    result[str(1)+' '+str(1)] = table[1][1]
    ans = func(len(table)-1, d, table, result)
    print(result.items())
    print(ans)


def func(c, d, table, result):
    #c = course 的數量
    #d = 總共有的天數
    if str(c)+' '+str(d) in result:
        return result[str(c)+' '+str(d)]
    if d > c and c != 0:
        value = []
        for i in range(1, d-(c-1)+1):
            value.append(func(c-1, d-i, table, result) + table[c][i])
        print(value)
        result[str(c)+' '+str(d)] = max(value)
        return result[str(c)+' '+str(d)]
    elif d == c and c!= 0:
        temp = 0
        for i in range(1, c+1):
            temp += table[i][1]
        result[str(c)+' '+str(d)] = temp
        return   result[str(c)+' '+str(d)]
    else:
        return 0

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

while True:
    #while 迴圈停在 '\n'
    table = [[-100, -100, -100, -100, -100],[-100, 3, 6, 7, 8],[-100, 4, 6, 9, 11],[-100,3, 4, 8, 9],[-100,6, 7, 9, 10]]
    result = {}
    #利用給定的 days 計算答案
    line = '7'
    while line.isdigit() != False:
        d = int(line)
        Arrange(table, result, d)
        line = ''
    if line == '':
        break
