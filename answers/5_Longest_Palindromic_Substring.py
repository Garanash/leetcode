# Крайне не эффективное решение
#
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest = s[0]
#         for i in range(len(s)):
#             for j in range(i+1, len(s)):
#                 substr = s[i:j+1]
#                 if substr == substr[::-1]:
#                     if len(substr) > len(longest):
#                         longest = substr
#         return longest


# Зачаток эффективного решения
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        m = len(s)
        if m == 2 and s[0] == s[1]:
            longest += s[1]
        for i in range(1, len(s)):
            stroka = s[i]
            l, k = i - 1, i + 1
            if k < m and l >= 0:
                substr1 = stroka + s[l]
                if substr1 == substr1[::-1]:
                    longest = substr1
                substr2 = stroka + s[l]
                if substr2 == substr2[::-1]:
                    longest = substr2
                if s[k] != s[l]:
                    if s[i] == s[k]:
                        stroka += s[k]
                        k += 1
                        if len(stroka) > len(longest):
                            longest = stroka
                    else:
                        continue
                while l >= 0 and k < m:
                    if s[l] == s[k]:
                        stroka = s[l] + stroka + s[k]
                        if len(stroka) > len(longest):
                            longest = stroka
                    l -= 1
                    k += 1
        return longest

st = Solution()
print(st.longestPalindrome('cbbd'))

