  #snake water gun game 
#                 S W G
# computer =     -1 0 1
# player = S -1 D W L
#          W  0 L D W 
#          G  1 W L D

import random
def check(comp,user):
    if comp == user:
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    return 1
    
comp = random.randint(0,2)
user = int(input(" for snake,1 for water and 2 foe gun:\n"))

score = check(comp,user)
print("you",user)
print("computer",comp)

if (score == 0):
    print("Darw")
elif(score == -1):
    print("lose")
else:
    print("you win")
