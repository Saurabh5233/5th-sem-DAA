# Print all leaf nodes of a Binary Search Tree using recursion

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_leaf_nodes(node):
    if not node:
        return

    if not node.left and not node.right:
        print(node.value, end=" ")

    print_leaf_nodes(node.left)
    print_leaf_nodes(node.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print("Leaf nodes of the BST are: ", end="")
print_leaf_nodes(root)
