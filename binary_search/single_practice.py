class Node:
    '''initial class for the node'''
    def __init__(self, data):
        self.data = data # data to store
        self.next = None # points to the next item
class linked_list:
    '''operations to manipulate nodes'''
    def __init__(self):
        self.head = None # first item in list
    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_item = self.head
        while last_item.next:
            #as long as there is a next item in our linked list, this is not our last item 
            last_item = last_item.next
        last_item.next = new_node
    def insert_at_middle(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        first_item = self.head
        length = 0
        while first_item.next is not None:
            length +=1
            first_item = first_item.next
        if length % 2 == 0:
            count = length/2
        else:
            count = (length +1) //2
        pointer = self.head
        while count >1:
            count -= 1
            pointer = pointer.next
        new_node.next = pointer.next
        pointer.next = new_node
    def insert_after_node(self, prev_node, new_data):
        if prev_node is None:
            print('The given previous node must be in the linked list')
        new_node = Node(new_data)
        if self.head == prev_node:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            current = self.head
            while current is not None:
                if current == prev_node:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next
    def print_list(self):
        start = self.head
        while start:
            print(start.data, end='')
            start = start.next


if __name__ == '__main__':
    llist = linked_list()

    # insert a series of new words into list
    llist.insert_at_start(1)
    llist.insert_at_end(2)
    llist.insert_at_end(4)
    llist.insert_at_end(5)
    llist.insert_at_end(6)

    llist.print_list()
    llist.insert_after_node(llist.head.next,3)
    llist.print_list()