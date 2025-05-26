class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        k = 0
        for elem in words:
            if x in elem:
                ans.append(k)
            k += 1
        return ans