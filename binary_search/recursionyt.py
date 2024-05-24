#!/usr/bin/env python3


def number(n):
    '''a function that prints numbers using recurssion'''
    if n == 5:
        print(n)
        return
    print(n)
    number( n+1)
def fibo(n): 
    '''calculate the nth fibonacci number'''    
    #base condition
    if (n < 2):
        return n
    return fibo(n-1) + fibo(n-2)

def bs(arr, target):
    ''' Function that implements binary search using recurssion'''
    