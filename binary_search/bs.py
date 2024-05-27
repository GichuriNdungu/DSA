#!/usr/bin/env python3
def binary(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        #so long as low is smaller than or equal to the high 
        mid = (low + high)/2
        if type(mid) == float:
            mid = int(mid)
        guess = list[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            low = mid - 1
        elif guess == item:
            return mid
        else: 
            return None

# my_list = [1,2,3,4,5,6]
# print(len(my_list))
# result = binary(my_list, 6)
# print(result)

def bs_recursive(arr, target, s, e):
    '''function that finds an item in an array using recurssion
    parameters:
        s: start
        e: end
        arr: array to search
        target: item to find in arr
    return:
        index of target'''
    if s > e:
        #means you have not found the answer
        return -1
    m = s + (e - s)//2
    if arr[m] == target:
        return m
    if target < arr[m]:
        # middle element is less than the target, so its in the left side of arr
        return bs_recursive(arr, target, s, m-1)
    else:
        # The target is in the right of arr, so start will be m+1
        return bs_recursive(arr, target, m+1, e)
    
def print_num(num):
    '''print numbers below a certain number'''
    print(num)
    if num == 0:
        return
    print_num(num-1)

def print_above(num):
    '''print numbers above num'''
    if num == 0:
        return
    print_above(num-1)
    print(num)
def print_both(num):
    if num == 0:
        return
    print(num)
    print_both(num-1)
    print(num)

def factorial(n):
    #number multiplied by every number below 
    # factorial n = n * f(n-1):
    if n <= 1:
        return 1
    else:
        return(n * factorial(n-1))
def sum(num):
    '''returns the sum of numbers below number'''
    if num <=1:
        return 1
    return num + sum(num-1)

def cumsum(n):
    '''Get the sum of the numbers in a digit'''
    if n == 0:
        return 0 
    return (n%10) + cumsum(n//10)

#quotient is gotten by using a double divisor