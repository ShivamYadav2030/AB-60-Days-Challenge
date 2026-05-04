class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

new_head = remove_nth_from_end(head, 2)

current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")