""" This is a project on a famous mathematical collatz conjecture"""
import matplotlib.pyplot as plt
import numpy as np
def collatz(num):
    result=num
    Lx=[]
    Ly=[]
    count=0
    while result!=1: #if num is even divide by 2
    #if num is odd 3n+1
        if result%2==0:
           result=result//2
           Lx.append(result)
        elif result%2==1:
            result=3*result+1
            Lx.append(result)
        count+=1 
        Ly.append(count)     
    
    return Lx,Ly

if __name__=='__main__':
    a=int(input("Enter Number you want to test:"))
    print(collatz(a))

    plt.scatter(collatz(a)[1],collatz(a)[0],s=2.5)
    plt.grid()
    plt.show()
    