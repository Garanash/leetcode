class Solution:
    def reverse(self, x: int) -> int:
        stroka = ""
        r = '-' if x < 0 else ''
        x = abs(x)
        while x > 0:
            stroka += str(x % 10)
            x //= 10
        res = int(stroka) * -1 if r else (int(stroka) if stroka else 0)
        if res > 2**31 or res < -2**31:
            return 0
        return res