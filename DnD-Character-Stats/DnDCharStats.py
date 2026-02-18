# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:39:05 2020
D&D 5E character stats roll

@author: eva
"""
import random

rolledStats=[]
for i in range(1,7):
    rolls=[]
    for j in range(4):        
        rolls.append(random.randint(1,6))
    sortedRolls=sorted(rolls)
    sortedRolls.pop(0)
    rolledStats.append(sum(sortedRolls))
    
print("Your rolled character stats are:")
print(' '.join(str(x) for x in rolledStats))