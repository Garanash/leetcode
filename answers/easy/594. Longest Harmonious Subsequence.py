class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = dict()
        for elem in nums:
            if elem in hashmap:
                hashmap[elem] += 1
            else:
                hashmap[elem] = 1
        sorted_hashmap = dict(sorted(hashmap.items()))

        max_l = 0
        f, k = -10 ** 11, 0
        for key, val in sorted_hashmap.items():
            if key - f == 1:
                max_l = max(max_l, abs(val + k))
            f = key
            k = val
        return max_l
