class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Dictionary to map original nodes to their cloned counterparts
        # e.g., { original_node_1: cloned_node_1 }
        old_to_new = {}
        old_to_new[node] = Node(node.val)
        
        # The stack should ONLY contain original nodes to guide our traversal
        dfs = [node]
        
        while dfs:
            curr = dfs.pop()
            
            # Look at the original node's neighbors
            for neighbor in curr.neighbors:
                # If we haven't cloned this neighbor yet
                if neighbor not in old_to_new:
                    # 1. Create the clone and store it in the map
                    old_to_new[neighbor] = Node(neighbor.val)
                    # 2. Add the ORIGINAL neighbor to the stack so we can explore it later
                    dfs.append(neighbor)
                
                # Link the cloned current node to the cloned neighbor
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]

