class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        left = 0
        right = len(heights) - 1
        while left != right:
            currVol = min(heights[left], heights[right]) * (right - left)
            if currVol > maxVol:
                maxVol = currVol
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxVol
        
        

        