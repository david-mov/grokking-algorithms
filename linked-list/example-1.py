class ListNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class SinglyLinkedList:
	def __init__(self, head = None):
		self.head = head

	def add_first(self, value):
		self.head = ListNode(value, self.head)

	def for_each(self, cb):
		pointer = self.head
		while pointer:
			cb(pointer.value)
			pointer = pointer.next

list = SinglyLinkedList()

list.add_first('groceries')
list.add_first('movie')
list.add_first('sfbc membership')

list.for_each(print)