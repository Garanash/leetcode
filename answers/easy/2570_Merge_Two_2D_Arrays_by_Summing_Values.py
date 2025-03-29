from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = nums1 + nums2
        res.sort()
        tr = [res[0]]
        for i in range(1, len(res)):
            if res[i][0] == tr[-1][0]:
                tr[-1] = [tr[-1][0], tr[-1][1] + res[i][1]]
            else:
                tr.append(res[i])
        return tr
