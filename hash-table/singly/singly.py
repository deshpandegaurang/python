from node import Node
import sys

class Singly:
    def __init__(self):
        self.head = self.tail = None
        self.my_list = self

    def insert_head(self , item):
        if self.is_empty(self.head):
            node_obj = Node(item)
            self.my_list.next = self.head = self.tail = node_obj
            return self.my_list
        else:
            node_obj = Node(item)
            node_obj.next = self.head
            self.head = node_obj

    def delete_item(self , item):
        if self.is_empty(self.head):
            return "this item cannot be deleted"
        else:
            current_node = self.head
            deleted = False
            while current_node.next != None:
                if current_node == self.head:
                    deleted = True
                    self.head = self.head.next
                    return item
                elif current_node.next == self.tail:
                    if self.tail.data == item:
                        deleted = True
                        current_node.next = None
                        return item
                elif current_node.next.data == item:
                    deleted = True
                    node_to_be_deleted = this.node.next
                    current_node.next = node_to_be_deleted.next
                    return item
            if not deleted:
                return "item not found"

    def is_empty(self , s_list):
        return s_list == None

    def get_list(self):
        if self.head == None:
            return "the list is empty"
        else:
            if self.head.next == None:
                return [self.head.data]
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
