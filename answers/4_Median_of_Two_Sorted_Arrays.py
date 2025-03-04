from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, k = len(nums1), len(nums2)
        new = sorted(nums1 + nums2)
        if (n + k) % 2 == 0:
            res = (new[(n + k) // 2] + new[(n + k) // 2 - 1]) / 2
        else:
            res = float(new[(n + k) // 2])
        return res