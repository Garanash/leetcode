class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n >= 1:
            r = 0
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                r += 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                r += 1
            for i in range(1,len(flowerbed)):
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    r += 1
            if r >= n:
                return True
            else:
                return False
        else:
            return True

