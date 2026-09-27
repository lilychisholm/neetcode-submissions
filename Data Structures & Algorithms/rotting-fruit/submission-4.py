class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #modify grid as we see fresh fruit
        #each fresh fruit we go to, edit the fruit so its value is instead (2, time) indicating the time it took to become rotten (distance)
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = (1, float('inf'))
                elif grid[i][j] == 2:
                    grid[i][j] = (2, 0)
                    queue.append((i, j))
                else:
                    grid[i][j] = (-1, -1)

        while queue:
            fruit = queue.pop()
            y = fruit[0]
            x = fruit[1]
            time = grid[y][x][1]

            if y + 1 < len(grid) and grid[y+1][x][1] > time:
                grid[y+1][x] = (2, time + 1)
                queue.append((y+1, x))
            if y - 1 >= 0 and grid[y-1][x][1] > time:
                grid[y-1][x] = (2, time + 1)
                queue.append((y-1, x))
            if x + 1 < len(grid[0]) and grid[y][x+1][1] > time:
                grid[y][x+1] = (2, time + 1)
                queue.append((y, x+1))
            if x - 1 >= 0 and grid[y][x-1][1] > time:
                grid[y][x-1] = (2, time + 1)
                queue.append((y, x-1))

        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j][1] == float('inf'):
                    return -1
                if grid[i][j][1] > maximum:
                    maximum = grid[i][j][1]

        return maximum
            

        
                



        
        