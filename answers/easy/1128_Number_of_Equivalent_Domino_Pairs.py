from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hash_map = dict()
        result = 0
        for elem in dominoes:
            if tuple(elem) in hash_map:
                result += hash_map[tuple(elem)]
                hash_map[tuple(elem)] += 1
            elif tuple(elem[::-1]) in hash_map:
                result += hash_map[tuple(elem[::-1])]
                hash_map[tuple(elem[::-1])] += 1
            else:
                hash_map[tuple(elem)] = 1
        return result


sl = Solution()
print(sl.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))