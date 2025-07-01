'''
1 for rock
0 for papper
-1 for seasor'''

import random
computer=random.choice([-1,0,1])
youstr=input("enter your choice:")
youDict={"r":1,'p':0,'s':-1}
reversedDict={1:"rock",0:"papper",-1:"seasor"}
you=youDict[youstr]
print(f" you chose {reversedDict[you]}\ncomputer chose {reversedDict[computer]}")
if(computer == you):
    print("its draw")
if (computer - you == -2 or computer - you == 1):
    print("You will lose")
else:
    print("You will win")
