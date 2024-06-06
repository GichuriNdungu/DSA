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
    '''Get the sum of the digits in a number'''
    if n == 0:
        return 0 
    return (n%10) + cumsum(n//10)

#quotient is gotten by using a double divisor

def digitprod(n):
    '''product of digits in a number'''
    #base case 
    if (n%10 == n):
        return n

    return (n%10) * digitprod(n//10)


class rev:
    sum = 0
    def revnum(self, n):
        '''reverses a number such that the last digit is the first'''
        
        if (n == 0):
            return
        self.sum = (self.sum *10) + n%10
        self.revnum(n//10)
        return self.sum
    
    
    

class zero_score():
    count = 0
    def num_zero(self, num):
        if num//10 <= 0:
            return
        if num %10 == 0:
            self.count += 1
        self.num_zero(num//10)
        return self.count

def steps(num, count):
    '''count steps to reduce number to 0'''
    #base
    if num == 0:
        return count
    #recursieve
    rem = num //2
    if num % 2 == 0:
        return steps(rem, (count + 1))
    else:
        return steps((num -1), (count +1))

