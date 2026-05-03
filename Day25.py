class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# Creating Linked List
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
head.next = second
second.next = third
third.next = fourth

fourth.next = second

if has_cycle(head):
    print("Cycle Detected")
else:
    print("No Cycle")