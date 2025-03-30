class Solution(object):
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}
        result = []
        maxLast, prevEnd = 0, -1

        for i, c in enumerate(s):
            maxLast = max(maxLast, last[c])
            if i == maxLast:
                result.append(i - prevEnd)
                prevEnd = i

        return result