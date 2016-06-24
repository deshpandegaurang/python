from hash_function import hash_function
from singly.singly import Singly

class HashTable:

    def __init__(self):
        self.my_hash_table = [None]*100
        self.length = len(self.my_hash_table)

    def insert(self , item):
        index = hash_function(self.length , item)
        print index
        if  self.my_hash_table[index] == None:
            singly_obj = Singly()
            self.my_hash_table[index] = singly_obj.insert_head(item)
        elif self.my_hash_table[index] != None:
            self.my_hash_table[index].insert_head(item)

    def delete(self , item):
        index = hash_function(self.length , item)
        target = self.my_hash_table[index]
        if target == None:
            return 'Nothing to deletepyto here'
        elif target.next.next == None:
            self.my_hash_table[index] = None
            return item
        else:
            return target.delete_item(item)

    def print_hash_table(self):
            index = 0
            for my_list in self.my_hash_table:
                if my_list == None:
                    print str(index) +' -> None'
                else:
                    print str(index) +' -> '+','.join(my_list.get_list())
                index = index + 1
