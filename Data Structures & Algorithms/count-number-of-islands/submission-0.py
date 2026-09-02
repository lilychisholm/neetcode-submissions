class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #look at each 1 and 0 as a node. for each 1 node, it will be numbered 0 to n-1. make an adjacency map to map each land node to its surrounding land nodes. then, do dfs on this adjacency map. each time the stack is emptied, we count 1 island.
        ones = defaultdict(list)
        ones_list = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    name = str(i) + " " + str(j)
                    ones_list.append(name)
                    if i > 0 and grid[i - 1][j] == "1":
                        item_name = str(i-1) + " " + str(j)
                        ones[name].append(item_name)
                    if i < len(grid)-1 and grid[i + 1][j] == "1":
                        item_name = str(i+1) + " " + str(j)
                        ones[name].append(item_name)                    
                    if j > 0 and grid[i][j - 1] == "1":
                        item_name = str(i) + " " + str(j-1)
                        ones[name].append(item_name)                        
                    if j < len(grid[i])-1 and grid[i][j + 1] == "1":
                        item_name = str(i) + " " + str(j + 1)
                        ones[name].append(item_name)

        dfs = []
        visited = set()
        islands = 0
        while ones_list != []:
            node = ones_list.pop()
            if node in visited:
                continue
            dfs.append(node)
            visited.add(node)
            islands += 1
            while dfs != []:
                new_node = dfs.pop()
                visited.add(new_node)
                for item in ones[new_node]:
                    if item not in visited:
                        dfs.append(item)

        return islands




