def is_balanced(node):
    if node is None:
        return True
    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)
    if abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False

def height_of_tree(node):
    if node is None:
        return 0
    else:
        return 1 + max(height_of_tree(node.left), height_of_tree(node.right))
