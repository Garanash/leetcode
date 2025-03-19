from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        m = len(nums)
        ml = 1
        for i in range(m - 1):
            k = 1
            pr = nums[i]
            for j in range(i + 1, m):
                if nums[j] & pr == 0:
                    pr = nums[j] | pr
                    k += 1
                    ml = max(k, ml)
                else:
                    break
        return ml
