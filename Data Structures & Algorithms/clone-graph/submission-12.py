class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        
        dfs = [node]
        
        while dfs:
            curr = dfs.pop()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    dfs.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]

