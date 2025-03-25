from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res_min = []
        res_max = []
        k = 0
        for elem in nums:
            if elem > pivot:
                res_max.append(elem)
            elif elem == pivot:
                k += 1
            else:
                res_min.append(elem)
        return res_min + [pivot for x in range(k)] + res_max
