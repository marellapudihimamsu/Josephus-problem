# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:41:18 2019

@author: Dell
"""
import matplotlib.pyplot as plt
ans=[]
for n in range(3,1000):
    ls=[]
    for i in range(n):
        ls.append(i)
    
    count=0
    i=0
    state=True     #true-taking knife   false-killing
    while(count!=n-1):
        if (i==n):
            i=0
        if(ls[i]==-1):
            i=i+1
            continue
        else:
            if(state):
                i=i+1
                state=False
            else:
                ls[i]=-1
                i=i+1
                count=count+1
                #print(ls)
                state=True
    for index in range(len(ls)):
        if ls[index]!=-1:
            print(index+1)
            ans.append(index+1)
plt.plot(ans,'r.')
plt.axis([0, 1000, 0, 1000])
plt.ylabel('person alive')
plt.xlabel('circle of size N')
plt.grid(True)


    
            
    