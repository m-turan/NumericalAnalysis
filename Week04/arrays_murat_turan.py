import random
import numpy as np

def replace_center_with_minus_one(d, n, m):
    if (m > n or d<=0 or n<0 or m<0):
        raise ValueError("Value Error!")
        
    numpy_array =random.randint(0,(10 ** d)-1,size=(n,n))
    print(numpy_array)
    first_idx=(n-m)//2
    last_idx=first_idx+m
    
    for i in range(first_idx,last_idx):
        for j in range(first_idx,last_idx):
            numpy_array[i][j]=-1

    return numpy_array
