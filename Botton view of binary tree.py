class Solution: 
    def bottomView(self, root): 
        # Queue to store (node, horizontal distance)
        queue = [[root, 0]]  
        ans = {}  # Dictionary to store the last node at each horizontal distance

        while queue:
            node = queue.pop(0)
            r = node[0]
            val = r.data
            col = node[1]
            ans[col] = val  # Store the last seen node at this horizontal distance

            # Move left with col - 1
            if r.left:
                queue.append([r.left, col - 1])
            # Move right with col + 1
            if r.right:
                queue.append([r.right, col + 1])

        # Sorting keys and getting values in order
        return [ans[i] for i in sorted(ans.keys())]

