from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m = len(nums)
        k = 0
        for i in range(m - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                k += 1
        if nums.count(1) == m:
            return k
        else:
            return -1
