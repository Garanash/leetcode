class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums) - 2):
            if (nums[i] + nums[i + 2]) == nums[i + 1] / 2:
                k += 1
        return k
