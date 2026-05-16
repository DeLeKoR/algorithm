class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            x = 0
            y = 0
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            if l2 is not None:
                y = l2.val
                l2 = l2.next
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next

        return dummy.next