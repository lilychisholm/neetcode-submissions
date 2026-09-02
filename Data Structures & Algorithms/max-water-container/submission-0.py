class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        back = len(heights) - 1
        container = 0
        while front < back:
            temp = min(heights[front], heights[back]) * (back - front)
            container = max(container, temp)
            if heights[front] <= heights[back]:
                front += 1
            else:
                back -= 1
        return container

        