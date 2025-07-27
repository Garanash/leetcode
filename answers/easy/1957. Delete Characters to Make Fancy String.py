class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = [s[0]]
        k = 1
        for i in range(1, len(s)):
            symbol = s[i]
            if symbol == ans[-1] and k == 2:
                continue
            elif symbol == ans[-1]:
                ans.append(symbol)
                k += 1
            else:
                ans.append(symbol)
                k = 1
        return ''.join(ans)