#!/usr/bin/env python3
def sorted(arr, index):
    '''determine whether an array is sorted or not'''
    #base case 
    if (index == (len(arr)-1)):
        return True
    #recurssive case
    return arr[index] <= arr[index + 1] and sorted(arr, index + 1)


def linear_search(arr, target, index):
    """find a target item in an array"""
    #base case
    if index == len(arr):
        return
    #recursive 
    if arr[index] == target:
        return index
    else:
        return linear_search(arr, target, index+1)
def find_index_rev(arr, target, index):
    '''find index by searching from the end of an array'''
    if index == -1:
        return
    if arr[index] == target:
        return index
    else:
        return find_index_rev(arr, target, index -1)
index_list = []

def find_all(arr, target, index):
    """find a target item in an array"""
    #base case
    if index == len(arr):
        return
    #recursive 
    if arr[index] == target:
        index_list.append(index)
    find_all(arr, target, index+1)
    return index_list

def find_all2(arr, target, index):
    """find a target item in an array"""
    ind_list = []
    #base case
    if index == len(arr):
        return ind_list
    #recursive 
    if arr[index] == target:
        ind_list.append(index)
    answers_from_below = find_all2(arr, target, index+1)
    ind_list.extend(answers_from_below)
    return ind_list

arr = [1, 2, 3, 4, 2, 5, 2, 5, 2]
target = 2
index = 0

print(find_all2(arr, target, index))



