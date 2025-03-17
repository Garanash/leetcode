from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        m = len(nums)
        if m % 2 != 0:
            return False
        k = set()
        for i in range(m):
            if nums[i] in k:
                k.remove(nums[i])
            else:
                k.add(nums[i])
        if k:
            return False
        return True
