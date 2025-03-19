from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        m = len(nums)
        for i in range(m - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        result = [x for x in nums if x != 0]
        result.extend([0 for x in range(m - len(result))])
        return result
