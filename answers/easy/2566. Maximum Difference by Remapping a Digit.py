class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxim = ''
        pr = str(num)
        for i, k in enumerate(pr):
            if pr[i] != '9':
                maxim = pr.replace(k,'9')
                break
        if not maxim:
            maxim = num
        else:
            maxim = int(maxim)
        minim = pr.replace(pr[0], '0')
        if not minim:
            minim = 0
        else:
            minim = int(minim)
        return maxim - minim if minim else maxim