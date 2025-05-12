class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        sp = []
        for i in range(100,1000,2):
            kp = digits[::]
            n = i
            flag = True
            while n > 0:
                if n % 10 not in kp:
                    flag = False
                    break
                else:
                    kp.remove(n % 10)
                n //= 10
            if flag:
                sp.append(i)
        return sp
