class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        difference = 0
        left = 0
        right = 1
        while left < len(prices) - 1:
            profit = prices[right] - prices[left]
            if profit <= 0 and right == left + 1:
                left += 1
                right += 1
            else:
                if profit > difference:
                    difference = profit
                if right == len(prices) - 1:
                    left += 1
                    right = left + 1
                else:
                    right += 1
        return difference

        

        
        