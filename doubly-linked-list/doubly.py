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

    def remove_tail(self):
        if self.tail ==  None:
            return "Nothing to delete here"
        else:
            if self.head == self.tail:
                return_data = self.head.data
                self.head = self.tail = None
            else:
                return_data = self.tail.data
                self.tail = self.tail.prev
                self.tail.next = None
            return return_data

    def remove_head(self):
        if self.head ==  None:
            return "Nothing to delete here"
        else:
            if self.head == self.tail:
                return_data = self.head.data
                self.head = self.tail = None
            else:
                return_data = self.head.data
                self.head = self.head.next
                self.head.prev = None
            return return_data

    def insert_to_index(self , index , data):
        if self.get_list_length() < int(index):
            print "You cannot break this code. Try again :P"
        elif int(index) == 0:
            self.insert_head(data)
        elif int(index) == self.get_list_length():
            self.insert_tail(data)
        else:
            to_be_next_node = self.get_to_be_next_node(index)
            prev_node = to_be_next_node.prev
            node_obj = Node(data)
            node_obj.next = to_be_next_node
            node_obj.prev = prev_node
            prev_node.next = node_obj
            to_be_next_node.prev = node_obj
            print "item inserted at index - "+str(index)

    def get_to_be_next_node(self , index):
        iterator_index = 0
        return_node = self.head
        while int(index) != iterator_index:
            return_node = return_node.next
            iterator_index = iterator_index + 1
        return return_node

    def get_list_length(self):
        return self.get_list(True)

    def get_list(self , length = None):
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
                    if length == None:
                        return data_list
                    else:
                        return len(data_list)
