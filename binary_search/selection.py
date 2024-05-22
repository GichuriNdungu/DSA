#!/usr/bin/env python3

def find_smallest(arr):
    '''find the smallest Item in an array'''
    smallest = arr[0]
    smallest_index = 0
    for element in range (1, len(arr)):
        if arr[element] < smallest:
            smallest = arr[element]
            smallest_index = element
    return smallest
def selection_sort(arr):
    '''performs selection sort on an array'''
    #objective, sort arr from smallest to largest
    #define an empty list
    new_arr = []
    #loop through array
    for i in range(len(arr)):
    # find smallest using find_smallest
        smallest = find_smallest(arr)
        #check if smallest is in new_arr
        if smallest not in new_arr:
            new_arr.append(smallest)
            #remove smallest from arr
            arr.remove(smallest)
    #return empty list
    return new_arr

print(selection_sort(arr= [10, 9, 8, 7, 6]))
