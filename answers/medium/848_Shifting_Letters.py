from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(letter, k):
            return chr((ord(letter) - 97 + k) % 26 + 97)
        s = list(s)
        k = len(s) - 1
        nak = 0
        for elem in shifts[::-1]:
            nak += elem
            s[k] = shift(s[k], nak)
            k -= 1
        return ''.join(s)


sl = Solution()
print(sl.shiftingLetters(s = "aaa", shifts = [1,2,3]))