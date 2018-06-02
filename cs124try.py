# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 16:06:08 2018

@author: zz
"""
import numpy as np
f = open('example_data_1.txt', 'r')
data=[]
for line in f:
    individual=[]
    line_content=line.strip()
    for snp in line_content.split(' '):
        individual.append(int(snp))
    data.append(individual)
myarray=np.array(data)
true_data=np.transpose(myarray)
mydict={}
for i in range(true_data.shape[0]):
    mydict[i]=[]
    mydict[i].append(true_data[i,:])
    mydict[i].append([])
    mydict[i].append([])
print len(mydict)   #50    
    
        
