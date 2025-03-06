from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        ml = min(strs, key=len)
        k = 0
        for i in range(len(ml)):
            bukva = strs[0][i]
            flag = True
            k += 1
            for j in range(len(strs)):
                if strs[j][i] != bukva:
                    flag =False
                    break
            if flag:
                pref += bukva
            else:
                return pref
        return pref
