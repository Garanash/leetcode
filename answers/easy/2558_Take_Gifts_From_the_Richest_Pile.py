from typing import List
from math import floor

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            maxim = max(gifts)
            gifts[gifts.index(maxim)] = floor(maxim ** 0.5)
        return sum(gifts)