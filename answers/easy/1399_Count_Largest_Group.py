class Solution:
    def sum_digit(self, n):
        res = 0
        while n > 0:
            res += n % 10
            n //= 10
        return res

    def countLargestGroup(self, n: int) -> int:
        sp = [[] for x in range(n+1)]

        for i in range(1,n+1):
            r = self.sum_digit(i)
            sp[r].append(i)
        mx = 0
        k = 1
        print(sp)
        for elem in sp:
            if len(elem) > mx:
                mx = len(elem)
                k = 1
            elif len(elem) == mx:
                k += 1
        return k

sl = Solution()
print(sl.countLargestGroup(2))