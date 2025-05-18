from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            if target > nums[j // 2]:
                i = j
            elif target < nums[j // 2]:
                j = j // 2
            else:
                return j // 2
        return j

sl = Solution()
print(sl.searchInsert(nums = [1,3,5,6], target = 7))