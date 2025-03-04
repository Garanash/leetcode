
# Не эффективное решение
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_dli = 0
#         for i in range(len(s)):
#             k = 1
#             stroka = s[i]
#             for j in range(i+1, len(s)):
#                 if s[j] in stroka:
#                     max_dli = max(max_dli, k)
#                     break
#                 k += 1
#                 stroka += s[j]
#         return max_dli

# Эффективное решение
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_dli = 0
        k = len(set(s))
        stroka = ''
        for i in range(len(s)):
            if s[i] in stroka:
                stroka = stroka[stroka.index(s[i])+1:] + s[i]
            else:
                stroka += s[i]
            max_dli = max(max_dli, len(stroka))
            if max_dli == k:
                break

        return max_dli
