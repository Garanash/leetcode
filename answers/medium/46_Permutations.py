from itertools import permutations

class Solution(object):
    def permute(self, nums):
        return [list(map(int,x)) for x in permutations(nums)]