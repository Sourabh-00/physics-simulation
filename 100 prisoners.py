import numpy as np
#for refrence probability that each of the 100 prisoners win by randomly selecting 50 boxes to check out of 100 boxes is (1/2)^100
rng=np.random.default_rng()
success=0
trials=10000
prisoners=100
max_chances=int(prisoners/2)
for t in range(0,trials):
    number=np.arange(0,prisoners,1)
    rng.shuffle(number)
    win=0
    for i in range(0,prisoners):
        j=i
        flag=0
        for chances in range(0,max_chances):
            if number[j]==i:
                win=win+1
                flag=1
                break
            else:
                j=number[j]
        if chances==max_chances-1 and flag==0:
            break
    if win==prisoners:
        #print('prisoners won')
        success=success+1
    #else:
        #print('prisoners lost')
print('probability of winning by looping method is: ',success/trials)
    

