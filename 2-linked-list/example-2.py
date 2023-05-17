class ListNode:
    def __init__(self, value, next = None):

        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def add_first(self, value):
        self.head = ListNode(value, self.head)

    def add_last(self, value):
        if (not self.head):
            self.head = ListNode(value)
        else:
            pointer = self.head
            while (pointer.next):
                pointer = pointer.next
            pointer.next = ListNode(value)

    def for_each(self, cb):
        if (not self.head):
            return False
        pointer = self.head
        while (pointer):
            cb(pointer.value)
            pointer = pointer.next

    def remove_first(self):
        if (self.head):
            self.head = self.head.next

    def remove_last(self):
        if (self.head):
            if (not self.head.next):
                self.head = None
            else:
                pointer = self.head
                while (pointer.next.next):
                    pointer = pointer.next
                pointer.next = None
            

list = SinglyLinkedList()

list.add_last('order one')
list.add_last('order two')
list.add_last('otder three')

list.remove_first()

list.for_each(print)