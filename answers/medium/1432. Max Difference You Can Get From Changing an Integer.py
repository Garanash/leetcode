class Solution:
    def maxDiff(self, num: int) -> int:
        pr = str(num)
        a = b = pr
        for symb in pr:
            if symb != '9':
                a = pr.replace(symb, '9')
                break
        for i, symb in enumerate(pr):
            if symb != '1' and symb != '0':
                if i != 0 and symb != pr[0]:
                    b = pr.replace(symb, '0')
                    break
                else:
                    b = pr.replace(symb, '1')
                    break
        return int(a) - int(b)

