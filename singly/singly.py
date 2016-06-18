from node import Node

class Singly:
    def __init__(self):
        self.head = self.tail = None

    def insert_head(self , item):
        if self.is_empty(self.head):
            node_obj = Node(item)
            self.head = self.tail = node_obj
        else:
            node_obj = Node(item)
            node_obj.next = self.head
            self.head = node_obj

    def insert_tail(self,item):
        if self.is_empty(self.tail):
            node_obj = Node(item)
            self.head = self.tail = node_obj
        else:
            node_obj = Node(item)
            self.tail.next = node_obj
            self.tail = node_obj

    def remove_head(self):
        if self.is_empty(self.head):
            return "You have nothing here!!"
        else:
            if self.head.next == None:
                return_item = self.head.data
                self.head = self.tail = None
            else:
                return_item = self.head.data
                self.head = self.head.next
            return return_item

    def remove_tail(self):
        if self.is_empty(self.tail):
            return "you have nothing here mate"
        else:
            if self.head.next == None:
                return_item = self.head.data
                self.head = self.tail = None
            else:
                iterator = self.head
                while True:
                    previous = iterator
                    iterator = iterator.next
                    if iterator.next == None:
                        return_item = iterator.data
                        previous.next = None
                        self.tail = previous
                        break
            return return_item

    def is_empty(self , s_list):
        return s_list == None

    def get_list(self):
        if self.head == None:
            return "the list is empty"
        else:
            if self.head.next == None:
                return self.head.data
            else:
                return_list = []
                iterator = self.head
                while True:
                    return_list.append(iterator.data)
                    iterator = iterator.next
                    if iterator.next == None:
                        return_list.append(iterator.data)
                        break
                return return_list
