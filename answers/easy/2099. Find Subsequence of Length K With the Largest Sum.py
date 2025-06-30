class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        while len(nums) != k:
            nums.pop(nums.index(min(nums)))
        return nums