class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        final_k = r

        while l <= r:
            potential_k = l + (r-l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / potential_k)
            if hours <= h:
                final_k = potential_k
                r = potential_k - 1
            else:
                l = (l + (r-l) // 2) + 1
        return final_k
        