class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        k = len(head)
        res = 0
        pr = head
        while head:
            res += 2 ** k * head.val
            k -= 1
            head = head.next
        return res