from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = [cell for row in grid for cell in row]
        a.sort()
        mid = len(a) // 2
        median = a[mid]
        tc = 0
        for value in a:
            if abs(value - median) % x != 0:
                return -1
            tc += abs(value - median) // x
        return tc
