class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def storeNodes(root, all_nodes, leaf_nodes):
    if root is None:
        return
    
    all_nodes.add(root.data)
    
    # If it's a leaf node, store it separately
    if root.left is None and root.right is None:
        leaf_nodes.add(root.data)
    
    storeNodes(root.left, all_nodes, leaf_nodes)
    storeNodes(root.right, all_nodes, leaf_nodes)

def isDeadEnd(root):
    if root is None:
        return False

    all_nodes = set()
    leaf_nodes = set()

    storeNodes(root, all_nodes, leaf_nodes)

    # Check for dead end condition
    for leaf in leaf_nodes:
        if (leaf - 1 in all_nodes) and (leaf + 1 in all_nodes):
            return True

    return False

# Example Tree
root = Node(8)
root.left = Node(5)
root.right = Node(9)
root.left.left = Node(2)
root.left.right = Node(7)
root.left.left.left = Node(1)

# Check for dead end
print("Yes" if isDeadEnd(root) else "No")
