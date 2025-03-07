class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0]*n
        elif k > 0:
            res = []
            for i in range(n):
                s = 0
                for j in range(k):
                    s += code[(i + j + 1) % n]
                res.append(s)
            return res
        else:
            res = []
            for i in range(n):
                s = 0
                for j in range(abs(k)):
                    s += code[i - j - 1]
                res.append(s)
            return res