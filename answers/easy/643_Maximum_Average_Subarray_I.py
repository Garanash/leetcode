class Solution(object):
    def findMaxAverage(self, nums, k):
        mr = r = sum(nums[:k])
        for i in range(k, len(nums)):
            r += nums[i] - nums[i - k]
            mr = max(mr, r)
        return mr / k

sl = Solution()
print(sl.findMaxAverage([1,12,-5,-6,50,3], 4))