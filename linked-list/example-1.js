class ListNode {
	constructor(value, next = null) {
		this.next = next 
		this.value = value
	}
}

class SinglyLinkedList {
	constructor(head = null) {
		this.head = head
	}

	addFirst(value) {
		this.head = new ListNode(value, this.head)
	} // O(1)

	traverse(cb) {
		let pointer = this.head
		while (pointer) {
			cb(pointer.value)
			pointer = pointer.next
		}
	} // O(n)
}

const list = new SinglyLinkedList()

list.addFirst('groceries')
list.addFirst('movie')
list.addFirst('sfbc membership')

list.traverse(console.log)
