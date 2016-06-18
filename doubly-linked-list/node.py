class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

    def get_next(self):
        if self.has_next():
            return self.next
        else:
            return False

    def get_prev(self):
        if self.has_prev():
            return self.prev
        else:
            return False

    def has_next(self):
        if self.next != None:
            return True
        else:
            return False

    def has_prev(self):
        if self.prev != None:
            return True
        else:
            return False
