#!/usr/bin/env python3
import random

def quicksort(arr):
    #base case: where len(arr) < 2
    if len(arr) < 2:
        return arr
    #define pivot
    mid = len(arr)//2
    pivot = arr[mid]
    #enter recurssive case
    less = []
    greater = []
    for element in arr[1:]:
        if element <= pivot:
            less.append(element)
    for element in arr[1:]:
        if element > pivot:
            greater.append(element) 
    return quicksort(less) + [pivot] + quicksort(greater)

arr = [58,25,58,96,100,56,21]
print(len(arr))
sorted = quicksort(arr)
print(len(sorted))
