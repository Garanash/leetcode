class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        sp = 1
        prev = nums[0]
        for i in range(len(nums)):
            if nums[i] - prev > k:
                sp += 1
                prev = nums[i]
        return sp