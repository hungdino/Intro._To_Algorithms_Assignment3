import numpy as np
def dynamic_programming3(table,table2,day,course):
    if(table2[day][course]!=-1):
        return table2[day][course]
    maxx=0
    for i in range(1,day-course+2):
        
        if(i>len(table)):
            break
        k = table[i-1][course-1] + dynamic_programming3(table,table2,day-i,course-1)
        
        if(maxx < k):
            maxx = k
    
    table2[day][course]=maxx
    
    return maxx
fin = open("input.txt","r",encoding="utf-8")

tmp_list=[]
flag=0;

while(1):
    while(1):
        table=[]
        r = 1
        while(1):#讀取矩陣
            s = fin.readline()
            if(s=='\n'):
                break
            if(s!=""):
                row = list(map(int,s.split(' ')))
                table.append(row)
            else:
                flag=1
                break
        if(flag==1):
            break
        row = len(table)
        course = len(table[0])
        column = len(table[0])
        q=2
        
        while(q):#讀取day
            q=q-1
            day = fin.readline()
            day=int(day.split('\n')[0])
            table2=[]
            
            li=[]
            for i in range(column+1):
                li.append(-1)
            table2.append(li)
            tmp=0
            for i in range(1,day+1):
                li=[]
                li.append(-1)
                for j in range(1,column+1):
                    if(i==j):
                        
                        tmp+=table[0][j-1]
                        
                        li.append(tmp)
                    else:
                        li.append(-1)
                table2.append(li)
            for i in range(1,day+1):
                if(i<=len(table)):
                    table2[i][1]=table[i-1][0]
                else:
                    table2[i][1]=0
            
            print(dynamic_programming3(table,table2,day,course))
            
                
                
            
            
            
            car=fin.readline()
    if(flag==1):
        break