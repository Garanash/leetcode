class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        p = n // 3
        t = 0
        res = []
        for i in range(p):
            res.append([])
            for j in range(n // p):
                if j == 0:
                    cm = nums[t]
                    res[i].append(nums[t])
                    t += 1
                else:
                    if nums[t] - cm > k:
                        return []
                    res[i].append(nums[t])
                    t += 1
        return res