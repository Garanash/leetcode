class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        r = 0
        md = 0
        for i in range(n):
            if blocks[i] == 'B':
                r += 1
                md = max(md, r)
            else:
                r = 0
        if md >= k:
            return 0
        else:
            min_k = k
            stroka = ''
            for i in range(n):
                if stroka.count('B') + stroka.count('W') < k:
                    stroka += blocks[i]
                else:
                    min_k = min(min_k, stroka.count('W'))
                    stroka = stroka[1:] + blocks[i]
            min_k = min(min_k, stroka.count('W'))
            return min_k

st = Solution()
print(st.minimumRecolors("WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", 15))