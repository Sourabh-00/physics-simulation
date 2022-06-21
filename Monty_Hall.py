# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:42:33 2022

@author: sourabh
"""
import random
import copy
t=0
playing=True
print("This is Monty Hall Problem")
print("There are three doors,behind one of the doors is a prize and other two are empty")
print("Goal of this game is to choose the door with a prize behind it")
while True:    
    #Chossing which door has prize behind it
    p=random.randint(1,3)
    x=int(input("choose the door out of 1,2 and 3    "))
    l=0
    i=0
    #scenario if the door choosen by participant is the door with thed prize
    if (x==p):
        t=copy.copy(p)
        #finding an empty door and openening it
        while (t==p):
            t=random.randint(1,3)
        print("The door which is empty is: ")
        print(t)
        l=copy.copy(t)
    else:
        #scenario if door choosen by participant is empty
        for i in range(1,4):
            #finding an empty door and openening it
            if (i!=x) and (i!=p):
                print("The door which is empty is: ")
                print(i)
                l=copy.copy(i)            
    print("choose the closed door you want to change to")
    print("type the same door number as previously choosen if you do not want to change")
    x=int(input("type here   "))
    #scenario if the participant chooses already opened empty door for second choice
    while x==l:
        x=int(input("you choose the already opened empty door you pea brained choose again: "))   
    #result
    if x==p:
        print("       YOU WIN       ")
    else:
        print("       LOSER        ")
    new_game=input("do you want to play again? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing")
        break
        