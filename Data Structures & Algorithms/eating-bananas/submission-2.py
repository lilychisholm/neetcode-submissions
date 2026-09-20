import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + (r-l) // 2
            timeCount = 0
            for p in piles:
                timeCount += math.ceil(float(p)/k)
            if timeCount <= h:
                res = k
                r = k -1
            else:
                l = k + 1
        return res
