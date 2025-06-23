class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)
        res = []
        x = 0
        while x < len(s):
            if x % k == 0:
                res.append(s[x])
            else:
                res[-1] += s[x]
            x += 1
        return res