class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_binary_tree(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:
        return True

    if not (min_value < node.value < max_value):
        return False

    return (
        is_binary_tree(node.left, min_value, node.value) and
        is_binary_tree(node.right, node.value, max_value)
    )

def build_tree_from_list(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    stack = [root]
    i = 1

    while i < len(lst) and stack:
        current = stack.pop(0)

        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            stack.append(current.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            stack.append(current.right)

        i += 1

    return root

# Example usage:
input_list = [2, 1, 3]
root = build_tree_from_list(input_list)

result = is_binary_tree(root)

if result:
    print("The given tree is a binary tree.")
else:
    print("The given tree is not a binary tree.")
