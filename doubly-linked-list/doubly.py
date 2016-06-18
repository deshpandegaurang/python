from node import Node

class Doubly:
    def __init__(self):
        self.head = self.tail = None

    def insert_head(self , data):
        if self.head == None:
            node_obj = Node(data)
            self.head = self.tail = node_obj
        else:
            old_head = self.head
            new_head = Node(data)
            new_head.next = old_head
            old_head.prev = new_head
            self.head = new_head

    def insert_tail(self , data):
        if self.tail == None:
            node_obj = Node(data)
            self.head = self.tail = node_obj
        else:
            old_tail = self.tail
            new_tail = Node(data)
            old_tail.next = new_tail
            new_tail.prev = old_tail
            self.tail = new_tail

    def get_list(self):
        if self.head == None:
            return "The List is empty pal"
        else:
            data_list = []
            iterator_index = self.head
            while iterator_index.has_next():
                data_list.append(iterator_index.data)
                iterator_index = iterator_index.next
                if not iterator_index.has_next():
                    data_list.append(iterator_index.data)
                    return data_list
