#!/usr/bin/env python3

def sum(arr, index=0):
    """find the sum of elements in an array"""
    #base case 
    if index == len(arr):
        return 0
    #recursive case
    return arr[index] + sum(arr, index + 1)

def total_elements(arr):
    """count the number of elements in list"""
    #base case 
    if len(arr) == 1:
        return 1
    return 1 + total_elements(arr[1:])


def max_in_list(arr, index = 0, max=0):
    """find the maximum number in a list"""
    #base case = no more items in list
    if index == len(arr):
        return max
    # recurssive
    if arr[index] > max:
        max = arr[index]
    return max_in_list(arr, index+1, max)

        