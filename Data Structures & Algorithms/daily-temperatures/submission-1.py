class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            curr = temperatures[i]
            if stack != []:
                while stack != [] and stack[-1][0] <= curr:
                    stack.pop()
            if stack != []:
                days = stack[-1][1] - i
                answer[i] = days
            stack.append([curr, i])

        return answer
        