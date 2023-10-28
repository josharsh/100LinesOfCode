""" This is a project on a famous mathematical collatz conjecture"""
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
def collatz(num):
    result=num
   # int(result)
    Lx=[]
    Ly=[]
    count=0
    while result!=1:
        if result%2==0: #if num is even divide by 2
           result=result//2
           Lx.append(result)
        elif result%2==1: #if num is odd 3n+1
            result=3*result+1
            Lx.append(result)
        count+=1 
        Ly.append(count)     
    
    return Lx,Ly

if __name__=='__main__':
    st.title("Collatz Conjecture")
    b=st.text_input("Enter Number you want to test:",value=1)
    st.write(b)
    a=int(b)
    data1={
        "X":collatz(a)[1],
        "Y":collatz(a)[0]
        } 
    with st.container():
     b=st.write(data1)
     ch=pd.DataFrame(data1)
     st.scatter_chart(ch)
    