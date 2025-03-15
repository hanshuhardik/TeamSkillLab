class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isDeadEnd(root, low=1, high=float('inf')):
    if not root:
        return False

    # Dead end condition
    if low == high:
        return True

    # Recursively check left and right subtrees
    return (isDeadEnd(root.left, low, root.data - 1) or 
            isDeadEnd(root.right, root.data + 1, high))

# Example Tree
root = Node(8)
root.left = Node(5)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(7)
root.left.left.left = Node(1)

# Check for dead end
print("Yes" if isDeadEnd(root) else "No")
