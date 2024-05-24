#!/usr/bin/env python3
def countdown(i):
    print(i)
    if i == 0:
        return
    countdown(i-1)

# countdown(i= 5)

def even_nums(num):
    '''print all the even nums below a number'''
    #define a base case 
    if num < 2:
        return
    #define recursive case 
    if num % 2 == 0:
        # even.append(num)
        new_num = num - 1
        print(num)
    else: 
        new_num = num - 1
            


even_nums(8)