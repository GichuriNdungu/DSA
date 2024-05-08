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

my_list = [1,2,3,4,5,6]
print(len(my_list))
result = binary(my_list, 6)
print(result)
