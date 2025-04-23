from functools import lru_cache


class Solution:

    @lru_cache
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            res = ''
            pr = self.countAndSay(n - 1)
            pr_symb = ''
            count = 0
            for i in range(len(pr)):
                if i == 0:
                    pr_symb = pr[i]
                    count += 1
                    continue
                if pr[i] != pr_symb:
                    res += str(count) + pr_symb
                    count = 1
                    pr_symb = pr[i]
                else:
                    count += 1
        if count >= 1:
            res += str(count) + pr_symb
        return res
