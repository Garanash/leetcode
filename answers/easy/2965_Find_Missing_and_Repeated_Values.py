from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        vstr = [0 for x in range(len(grid) * len(grid[0]) + 1)]
        r = m = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vstr[grid[i][j]]:
                    r = grid[i][j]
                else:
                    vstr[grid[i][j]] = 1
                vstr[grid[i][j]] = 1
        for i in range(len(vstr)):
            if vstr[i] == 0:
                m = i
        return [r, m]
