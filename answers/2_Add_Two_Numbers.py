from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        curr = new
        extra = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            total = a + b + extra
            extra = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
        if extra:
            curr.next = ListNode(extra)
        return new.next
