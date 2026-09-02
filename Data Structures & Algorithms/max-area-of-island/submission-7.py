class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ones = defaultdict(list)
        ones_list = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    name = str(i) + ' ' + str(j)
                    ones_list.append(name)
                    if i > 0 and grid[i-1][j] == 1:
                        temp_name = str(i-1) + " " + str(j)
                        ones[name].append(temp_name)
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        temp_name = str(i + 1) + " " + str(j)
                        ones[name].append(temp_name)
                    if j > 0 and grid[i][j - 1] == 1:
                        temp_name = str(i) + " " + str(j-1)
                        ones[name].append(temp_name)
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        temp_name = str(i) + " " + str(j + 1)
                        ones[name].append(temp_name)
                    
        visited = set()
        dfs = []
        max_island = 0
        while ones_list != []:
            node = ones_list.pop()
            if node in visited:
                continue
            dfs.append(node)
            temp_size = 0
            while dfs != []:
                new_node = dfs.pop()
                if new_node in visited:
                    continue
                visited.add(new_node)
                temp_size += 1
                for item in ones[new_node]:
                    if item not in visited:
                        dfs.append(item)
            if temp_size > max_island:
                max_island = temp_size

        return max_island

