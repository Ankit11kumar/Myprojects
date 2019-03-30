# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:04:30 2018

@author: ANKIT
"""

import xlrd
from collections import Counter


print("Please enter 3 symptoms\n")
s1=input("First symptom\n")
s2=input("Second symptom\n")                # this block takes symptoms as input
s3=input("Third symptom\n")

ds = xlrd.open_workbook(r'C:\Users\ANKIT\Downloads\C++\C++\file\dis-sym.xls')
d1=ds.sheet_by_index(0)
dnr1=d1.nrows                                 # this block opens sheet and counts its rows and columns
dnc1=d1.ncols

d=[]
for i in range(0,dnr1):
    for j in range(1,dnc1):                  # this block is for matching symptoms
        a=d1.cell_value(i,j)
        if((a==s1)or(a==s2)or(a==s3)):
            d.append(i)                     # this line..for storing corresponding row no. in a freq list
            
count=Counter(d)
max=count.most_common() 
print(max)                                    # this block..for counting most frequently occured row no. 
diseases=d1.cell_value(max[0][0],0)
print("\nYou are suffering with--\n",diseases)  # printing corresponding row and its zeroth column i.e disease


# for prescribing medicines

dm=xlrd.open_workbook(r'C:\Users\ANKIT\Downloads\C++\C++\file\dis-med.xls')
d2=dm.sheet_by_index(0)
dnr2=d2.nrows
dnc2=d2.ncols

m=[]
for i in range(1,dnr2):
    b=d2.cell_value(i,0)
    if(b==diseases):
        break

print("Your prescribed medicines are--\n")
for j in range(1,dnc2):
    m.append(d2.cell_value(i,j))
    print(d2.cell_value(i,j))


dc=xlrd.open_workbook(r'C:\Users\ANKIT\Downloads\C++\C++\file\med-cos.xls')        
d3=dc.sheet_by_index(0)
dnr3=d3.nrows
dnc3=d3.ncols

size=len(m)
cost=0
print(m)
for i in range(0,size):        
    for j in range(0,dnr3):
        if(m[i]==d3.cell_value(j,0)):
            print(m[i],d3.cell_value(j,0))
            cost=cost+d3.cell_value(j,2)
            
print(cost)
    
    
