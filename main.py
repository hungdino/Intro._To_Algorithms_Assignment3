# -*- coding: utf-8 -*-

def Arrange(table, result, d):
    print("There are ", d, " days")


def f(c, d, table, result):
    #c = course 的數量
    #d = 總共有的天數
    print()

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

f = open("input.txt", 'r')
line = f.readline()
while True:
    table_str = []
    #儲存 Table
    while line != '\n':
        table_str.append(line.split())
        line = f.readline()
    #while 迴圈停在 '\n'
    table = InitTable(table_str)
    result = {}
    line = f.readline()
    line = line.strip('\n')
    #利用給定的 days 計算答案
    while line.isdigit() != False:
        d = int(line)
        Arrange(table, result, d)
        line = f.readline()
        line = f.readline()
        line = line.strip('\n')
    if line == '':
        break
f.close()
