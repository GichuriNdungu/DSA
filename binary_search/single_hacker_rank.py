#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtTail(head, data):
    '''head: head of list'''
    #self.next for the last node should point to the new item
    new_node = SinglyLinkedListNode(node_data=data)
    pointer = head
    if pointer is None:
        pointer = new_node
    #if list is not empty, pointer of last item should point to new item
    # find last_item(self.next is none)
    first_item = head
    while first_item.next:
        next_item = first_item.next()
        first_item = next_item
    last_item = first_item
    last_item.next = new_node
    return pointer

n = int(input().strip())
head = None
for _ in range(n):
    data = int(input.strip())
    head = insertNodeAtTail(head, data)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
