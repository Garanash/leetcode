class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        k = -1
        res = 0
        pr = head
        while pr:
            k += 1
            pr = pr.next
        while head:
            res += 2 ** k * head.val
            k -= 1
            head = head.next
        return res