class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minim, md = nums[0], 0
        for i, num in enumerate(nums[1:]):
            if num <= minim:
                minim = num
            else:
                md = max(md, num - minim)
        return md if md > 0 else -1