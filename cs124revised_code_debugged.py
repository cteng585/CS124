# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 18:34:24 2018

@author: zz
"""
""" Class data structure section and main sections are only included for testing the code.
Clark's Method Implementation (doesn't calculate for genotypes with 2+ heterozygous positions
that are not explained by the list of "known haplotypes" """

from random import *

class genotype_data:
    haplotype1 = ''
    haplotype2 = ''
    genotype = ''
    position = 0
    def addGenotype(self, data):
        self.genotype = data
    def addHaplotype1(self, data):
        self.haplotype1 += data
    def addHaplotype2(self, data):
        self.haplotype2 += data

#Finding genotypes with less than 2 heterozygous positions
def L2H(genotype_data):
    count = 0
    for i in genotype_data:
        if i == '1':
            count += 1
    return(count)

#Generates all the possible phases for genotypes that have 1 or less heterozygous positions.
#Adds the 2H+ genotypes to a separate list
def generatePhases(genolist,phaselist,M2Hlist):
    #every_geno_has_at_least_2_hetero=False
    for elem in range(len(genolist)):
        data = genolist[elem].genotype
        if L2H(data) == 0:
            mystr=data.replace(2,1)
            if mystr not in phaselist:
                phaselist.append(data.replace('2','1'))
        elif L2H(data) == 1:
            #Included randomization, to prevent biases of always choosing "0" first to explain a heterozygous position
            x = randint(1,100)
            string1=''
            string2=''
            for q in range(len(data)):
                if data[q]=='0':
                    string1=string1+'0'
                    string2=string2+'0'
                elif data[q]=='2':
                    string1=string1+'1'
                    string2=string2+'1'
                elif data[q]=='1':
                    string1=string1+'1'
                    string2=string2+'0'
            
            if x > 49:
                tempstring = string1
                string1 = string2
                string2 = tempstring
            if string1 not in phaselist:
                phaselist.append(string1)
            if string2 not in phaselist:
                phaselist.append(string2)
        else:
            if data not in M2Hlist:
                M2Hlist.append(data)
                
#    if phaselist==[]:
#        every_geno_has_at_least_2_hetero=True
#        for e in range(len(genolist)):
#            data = genolist[elem].genotype  
#                if L2H(data)==2:
                    
                
             
            

#Remove duplicates which appear in a list
def removedup(list):
    nodup = []
    for elem in list:
        if elem not in nodup:
            nodup.append(elem)
    return(nodup)
    
  

def findmatch(h,g):
    find_already=False
    j=0
    for i in range(len(g)):
        if int(g[i])==2 and int(h[i])==1:
            j=j+1
        elif int(g[i])==0 and int(h[i])==0:
            j=j+1
        elif int(g[i])==1 and int(h[i])==1:
            j=j+1
        elif int(g[i])==1 and int(h[i])==0:
            j=j+1   
    if j == len(g):
         find_already=True
    return find_already


def findCompatibleHaplotype(Haplolist, Genotype):
    Additional_haplotypes_we_need=[]
    
    for i in range(len(Genotype)):
      the_matching_haplo=[]  
      find_one_match=False
      find_the_other_match=False
      j=0
      k=0
      for j in range(len(Haplolist)):
        find_one_match=False  
        if find_the_other_match==False: 
            
          if findmatch(Haplolist[j],Genotype[i]):
                      find_one_match=True
                      the_matching_haplo.append(Haplolist[j])
          if find_one_match: 
              for k in range(len(Haplolist)):
                pair=''
                for l in range(len(Haplolist[0])):
                    if int(Haplolist[j][l])+int(Haplolist[k][l])==1:
                        pair=pair+str(1)
                    elif int(Haplolist[j][l])+int(Haplolist[k][l])==2:
                        pair=pair+str(2)
                    else: 
                        pair=pair+str(0)
                if pair==Genotype[i]:
                    find_the_other_match=True
                    break
        else:
            break
        
      if j==(len(Haplolist)-1) and k==(len(Haplolist)-1):
          if find_the_other_match==False and the_matching_haplo!=[]:
              haplo1=the_matching_haplo[0]
              haplo2=''
              for s in range(len(Genotype[i])):
                  num=int(Genotype[i][s])-int(haplo1[s])
                  haplo2=haplo2+str(num)
                  
              Additional_haplotypes_we_need.append(haplo2)    
      if the_matching_haplo==[]:
              
              haplo1=''
              haplo2=''
              for f in range(len(Genotype[i])):
                  if Genotype[i][f]=='2':
                      haplo1=haplo1+'1'
                      haplo2=haplo2+'1'
                  elif Genotype[i][f]=='1':
                      haplo1=haplo1+'1'
                      haplo2=haplo2+'0'
                  else:
                      haplo1=haplo1+'0'
                      haplo2=haplo2+'0'
              Additional_haplotypes_we_need.append(haplo1)         
              Additional_haplotypes_we_need.append(haplo2)         
      
      
                   
    return(Additional_haplotypes_we_need)    
#Finds the remaining haplotypes which could describe the genotypes that have more than 1 heterozygous positions,
#using the list of known haplotypes.

    
    
    
    
    
    
# "Master Function" Which ends up generating a unique set of Haplotypes that are described by the given set of genotypes
def generateKnownHaplotypes(data):
    phase = []
    M2HList = []
    generatePhases(data,phase,M2HList)
    norepeatphase= removedup(phase)
        
    phase = []

#Proceed to find the remaining haplotype phases which explain the genotypes with more than one heterozygous position
#only adds additional haplotypes, if pre-exiting haplotype explains the genotype.
    for elem in M2HList:
        newhaplo = findCompatibleHaplotype(norepeatphase,[elem])
        for each_new_haplotype in newhaplo:
            if each_new_haplotype not in norepeatphase:
                norepeatphase.append(each_new_haplotype)
    

    return(norepeatphase)

def main():
    list=['01000']
    #list = ['11210','01000','11110','02100','20210']
    #list=['10210']
    #list=['12211','10210','10000','02100']
    newlist = []
    for elem in list:
        d = genotype_data()
        d.addGenotype(elem)
        newlist.append(d)

    KnownHaplotypes = generateKnownHaplotypes(newlist)
    print(KnownHaplotypes)

    # ['11210','01000','11110','02100','20210'] => Should contain only 01000, 01100, 10110, 10100, 00000
    # ['12211','10210','10000','02100'] => Cannot be computed by Clark's Algorithm. Added phases before termination: 
    #                                      10000, 00000, 01000, 01100, 11111

main()
