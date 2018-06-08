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
        if len(snp)!=0:
           individual.append(int(snp))
           
    data.append(individual)
myarray=np.array(data)
true_data=np.transpose(myarray)
#print true_data.shape
#print true_data.shape


#n=int(:
    #process_window(true_data[])             #seperate windows   

def count_hetero(array_data):    #input as np.array (n,1)
    count=0
    for i in range(array_data.shape[0]):
        if array_data[i]==1:
            count=count+1
    return count 

def generate_permute(l):  # input as [1,1,1]
    if l==[1]:
        return [[0],[1]]
    else:
        smallerlistlarger=[]
        for smallerlist in generate_permute(l[1:]):
            smallerlistlarger.append([0]+smallerlist)
            smallerlistlarger.append([1]+smallerlist)
        return smallerlistlarger

def create_unique_pair(l):  #input a list of haplo
    mypairs=[]
    #mypairsnew=[]
    #set_list=[]
    for i in range(len(l)):
        
        thepair=[]
        for j in range(len(l[i])):
           n=1-l[i][j]
           thepair.append(n)
        if  [l[i],thepair]  not in mypairs and [thepair,l[i]] not in mypairs:
             mypairs.append([l[i],thepair])
        
        
        
        
            
    return mypairs   

        
def create_pairs_haplos(data_array):   #np.array shape (n,1)
    current_hetero_index=0
    #calculate which hetero position we are currently visiting.
    
    generated_haplo_pair_list=[]
    for i in range(2**(count_hetero(data_array)-1)):
        generated_haplo_pair_list.append([[],[]])
    #generated_haplo_pair_list=[]
    
    l=[]
    len_hetero=count_hetero(data_array)
    for i in range(len_hetero):
        l.append(1)
    single_haplo_list=generate_permute(l)
    hetero_pairs=create_unique_pair(single_haplo_list)
    for i in range(data_array.shape[0]):
        if data_array[i]==1:
            for p in range(len(hetero_pairs)):
                generated_haplo_pair_list[p][0].append(hetero_pairs[p][0][current_hetero_index])
                generated_haplo_pair_list[p][1].append(hetero_pairs[p][1][current_hetero_index])
            current_hetero_index=current_hetero_index+1
        elif data_array[i]==0:
            generated_haplo_pair_list[p][0].append(0)
            generated_haplo_pair_list[p][1].append(0)
        else:
           generated_haplo_pair_list[p][0].append(1)
           generated_haplo_pair_list[p][1].append(1)
            
    return generated_haplo_pair_list      
    
        
        
    
        
        
        
        
       
def process_window(data):
    haplo_output=np.array(data.shape[0]*2,data.shape[1])
    mydict={}
    compatible_haplo_pairs=[]
    for i in range(data.shape[0]):
        compatible_haplo_pairs.append(0)
    
    for i in range(data.shape[0]):            #for 1 person
        compatible_haplo_pairs[i]=create_pairs_haplos(data[i,:])
    all_compatible_haplos=[]
    for i in range(data.shape[0]):
        for pair in compatible_haplo_pairs[i]:
            if pair[0] not in all_compatible_haplos:
                all_compatible_haplos.append(pair[0])
            if pair[1] not in all_compatible_haplos:
                all_compatible_haplos.append(pair[1])   
    mydict={}
    for haplo in all_compatible_haplos:
        mydict[haplo]=1.0/len(all_compatible_haplos)    #initialization
    mydict2_list=[]   #a list of prob dictionary for haplo pairs in each genotype
    for i in range(data.shape[0]):
        mydict2={}
        for j in range(len(compatible_haplo_pairs[i])):    #initialization
             mydict2[compatible_haplo_pairs[i][j]]=1.0/len(compatible_haplo_pairs[i])
        mydict2_list.append(mydict2)
    not_converge=True
    change_prob=[]
    for i in range(len(all_compatible_haplos)):
        change_prob.append[0]
    for i in range(1000):
        
          for j in range(len(all_compatible_haplos)):
              if change_prob[j]>0.01:
                  
                  break
              if j==len(all_compatible_haplos)-1:
                  not_converge=False
          if not_converge==False:
              break
          if not_converge:
              new_prob_dict={}
              for c in range(len(all_compatible_haplos)):
                  prob_sum=0
                  for x in range(data.shape[0]):
                      find_in_this_geno=False
                      for o in mydict2_list[x]:
                          if all_compatible_haplos[c] in o:
                              if count_hetero(data[x,:])==0:
                                  prob_sum=prob_sum+2.0*mydict2_list[x][o]
                              else:
                                  prob_sum=prob_sum+mydict2_list[x][o]
                              find_in_this_geno=True
                              break    
                  prob_sum=prob_sum/(2.0*data.shape[0])
                  change_prob[c]=abs(prob_sum-mydict[c])
                  mydict[c]=prob_sum
              for f in range(len(data.shape[0])):
                  total_p=0
                  for p in mydict2_list[f]:
                      total_p=total_p+mydict[p[0]]*mydict[p[1]]
                  for p in mydict2_list[f]:
                      mydict2_list[f][p]=mydict[p[0]]*mydict[p[1]]*1.0/total_p
                   
    for t in range(data.shape[0]):
           for u in compatible_haplo_pairs[t]:
               if mydict2_list[t][u]==max(mydict2_list[t][f] for f in compatible_haplo_pairs[t]):
                     haplo_output[2*t,:]= u[0]
                     haplo_output[2*t+1,:]=u[1]
                     break
    
    return haplo_output                 
                                  
                              
                                  
                      
                      
                  
                  
                  
                  
             
        
        
        
   
    
        
