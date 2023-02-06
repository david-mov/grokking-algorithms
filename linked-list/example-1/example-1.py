class ListNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class SinglyLinkedList:
	def __init__(self, head = None):
		self.head = head

	def addFirst(self, value):
		self.head = ListNode(value, self.head)

	def traverse(self, cb):
		pointer = self.head
		while pointer:
			cb(pointer.value)
			pointer = pointer.next

list = SinglyLinkedList()

list.addFirst('groceries')
list.addFirst('movie')
list.addFirst('sfbc membership')

list.traverse(print)