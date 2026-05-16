class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        current = second

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first = head
        second = prev

        while second is not None:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
