class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = s[:k]
        hashmap = {
            'a':start.count('a'),
            'e':start.count('e'),
            'i':start.count('i'),
            'o':start.count('o'),
            'u':start.count('u'),
        }
        max_v = sum(hashmap.values())
        for i in range(k, len(s)):
            if start[0] in hashmap.keys():
                hashmap[start[0]] -= 1
            start = start[1:] + s[i]
            if s[i] in hashmap.keys():
                hashmap[s[i]] += 1
            max_v = max(max_v, sum(hashmap.values()))
        return max_v