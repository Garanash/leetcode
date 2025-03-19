def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(3,round(num ** 0.5)+1, 2):
        if num % i == 0:
            return False
    return True

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left == 1 and right >= 3:
            return [2,3]
        res = []
        if left % 2 == 0:
            left += 1
        for i in range(left, right + 1, 2):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                continue
            if prime(i):
                if len(res) < 2:
                    res.append(i)
                else:
                    if i - pred < res[1] - res[0]:
                        res = [pred, i]
                        if i - pred == 2:
                            return res
                pred = i
        if len(res) < 2:
            return [-1,-1]
        return sorted(res)
