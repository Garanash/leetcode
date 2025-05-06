class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        m = len(nums)
        new = [0] * m
        for i in range(m):
            new[i] = nums[nums[i]]
        return new