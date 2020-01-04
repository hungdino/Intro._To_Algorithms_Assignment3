# -*- coding: utf-8 -*-
def Arrange(table, d):
    showTable(table)
    print("There are ", d, " days")
    


def showTable(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j], ' ', end='')
        print()

f = open("input.txt", 'r')
line = f.readline()
#print(type(line))
while True:
    table = []
    #儲存 Table
    while line != '\n':
        #print("I am ",line)
        #print("The len of this line: ", len(line))
        table.append(line.split())
        line = f.readline()
    #while 迴圈停在 '\n'
    #print("I am ", line, " the happy end")
    #print(table)
    showTable(table)
    line = f.readline()
    line = line.strip('\n')
    #利用給定的 days 計算答案
    while line.isdigit() != False:
        d = int(line)
        Arrange(table, d)
        line = f.readline()
        line = f.readline()
        line = line.strip('\n')
    if line == '':
        break
f.close()
