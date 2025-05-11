class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        k = 0
        for elem in arr:
            if elem % 2 != 0:
                k += 1
            else:
                k = 0
            if k == 3:
                return True
        return False
