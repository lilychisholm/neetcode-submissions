class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #need to make adjecency list of all treasure chests and islands and their surrounding up, down, left, and right
        #while traversing, each entry should include the x, y, and distance to the nearest chest
        #chests have a distance of 0
        #for each new things traversed, push with a distance of the parent items distance + 1
        #if you traverse to something that has already been visited, only push to the queue if the new distance would be less than the current distance

        treasure_nodes = deque()


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    treasure_nodes.append((i, j))

        while treasure_nodes:
            node = treasure_nodes.popleft()
            y = node[0]
            x = node[1]

            distance = grid[y][x]

            if y + 1 < len(grid) and grid[y+1][x] != -1 and grid[y+1][x] > distance + 1:
                treasure_nodes.append((y+1, x))
                grid[y+1][x] = distance + 1

            if y - 1 >= 0 and grid[y-1][x] != -1 and grid[y-1][x] > distance + 1:
                treasure_nodes.append((y-1, x))
                grid[y-1][x] = distance + 1

            if x + 1 < len(grid[0]) and grid[y][x+1] != -1 and grid[y][x+1] > distance + 1:
                treasure_nodes.append((y, x+1))
                grid[y][x+1] = distance + 1

            if x - 1 >= 0 and grid[y][x-1] != -1 and grid[y][x-1] > distance + 1:
                treasure_nodes.append((y, x-1))
                grid[y][x-1] = distance + 1

            

        
                    

        



        