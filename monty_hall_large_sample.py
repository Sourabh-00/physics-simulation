# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:42:33 2022

@author: sourabh
"""
import random
import copy
import time
print("This is Monty Hall Problem")
print("There are three doors,behind one of the doors is a prize and other two are empty")
print("Goal of this game is to choose the door with a prize behind it")  
n=int(input("Number of iterations? "))
start_time=time.time()
nochange=0
change=0
for j in range(1,n+1):
    doors=[1,2,3]
    t=0
    m=0
    p=random.choice(doors)
    x=random.choice(doors)
    l=0
    i=0
    if (x==p):
        t=copy.copy(p)
        while (t==p):
            t=random.choice(doors)
        #print("The door which is empty is: ")
        #print(t)
        l=copy.copy(t)
    else:
        for i in range(1,4):
            if (i!=x) and (i!=p):
                #print("The door which is empty is: ")
                #print(i)
                l=copy.copy(i)            
    #print("choose the closed door you want to change to")
    #print("type the same door number as previously choosen if you do not want to change")
    doors.remove(l)
    m=random.choice(doors)
    if m==p:
        #print("       YOU WIN       ")
        if m==x:
            nochange=nochange+1
        else:
                change=change+1
    else:
        #print("       LOSER        ")
        if m==x:
            change=change+1
        else:
                nochange=nochange+1
print("Probability of winning by changing the door is: ",(change/n))
print("probability of winning by staying at same door is: ",(nochange/n))
print("--- %s seconds ---" % (time.time() - start_time))
    