class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        maximum = 0
        for i in range(1, len(nums)):
            r = abs(nums[i - 1] - nums[i])
            if r > maximum:
                maximum = r
        return maximum