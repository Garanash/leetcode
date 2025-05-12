from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [x % 2 for x in nums]
        prefix_count = [0] * (len(nums) + 1)
        prefix_count[0] = 1
        s = 0
        ans = 0

        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        return ans



sl = Solution()
print(sl.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))