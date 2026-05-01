class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Creating Linked List: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# Reverse Linked List
reversed_head = reverse_linked_list(head)

current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")