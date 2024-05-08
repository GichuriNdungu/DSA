#!/usr/bin/env python3
class node:
    '''class that defines a singular node'''
    def __init__(self, data):
        '''data: data to be stored'''
        self.data = data
        self.next = None
class linked_list:
    '''class encapsulating all the operations to manage nodes'''
    def __init__(self):
        self.head = None # head == first item in list
    def insert_at_start(self, new_data):
        '''method to insert a new element at the start of the list'''
        new_node = node(data=new_data) # create a new node with data as new_data
        new_node.next = self.head # parameter next is set to the head
        self.head = new_node # the head is set to the new node just created.
    def insert_at_end(self, new_data):
        '''method to insert new element at the end of a list'''
        new_node = node(data=new_data)
        if self.head is None:
            self.head = new_node
            return
        last_item = self.head
        while last_item.next: 
            last_item = last_item.next # so long as there is a next item the next item will be the last, until there next is null
        last_item.next = new_node
    def insert_at_middle(self, new_data):
        '''method to insert item in the middle of a list'''
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        #calculate the length of the linked list
        next_item = self.head
        length = 0
        while next_item.next is not None:
            # so long as there is a next item, increase the lenght by one, then move to the next itemu
            length +=1
            next_item = next_item.next
        # count the number of nodes after which to insert the new item
        if length % 2 == 0:
            count = length//2
        else: 
            count = (length + 1)//2
        pointer = self.head
        while count >1:
            # so long as count is greater than one, reduce the count by one, and traverse through the list until count is zero 
            count -=1 
            pointer = pointer.next
        # insert the item here
        new_node.next = pointer.next
        pointer.next = new_node
    def print_list(self):
        '''method to print the newly created linked list'''
        temp = self.head #start at with the head of the list
        while temp:
            print(temp.data, end='') #print the data of the head
            temp = temp.next #set new temp to the next item
        print()
    def delete_from_end(self):
        # check if the list is empty
        if self.head is None:
            return "The list is empty"
        if self.head.next is None: # if there is only one node, then return null, successfully deleting the node and list 
            self.head = None
            return 
        temp = self.head
        if temp.next.next:
            # check if the next item has a next item after it. intution: the last item will not have a next.next
            temp = temp.next # update the temp up to the second last item
        # now make temp point to none, essentially deleting the last item
        temp.next = None

if __name__ == '__main__':
    llist = linked_list()

    # insert a series of new words into list
    llist.insert_at_start('fox')
    
    llist.insert_at_start('quick')
    llist.insert_at_start('The')
    llist.insert_at_end('jumps')
    llist.insert_at_end('over')

    llist.print_list()

    llist.insert_at_middle('brown')
    llist.delete_from_end()
    llist.print_list()
