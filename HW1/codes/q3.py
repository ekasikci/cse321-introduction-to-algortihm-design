from BST import BST

bst = BST()
bst.insert(1)
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(8)


bst2 = BST()
bst2.insert(9)
bst2.insert(10)
bst2.insert(14)
bst2.insert(13)
bst2.insert(15)
bst2.insert(16)
bst2.insert(12)
bst2.insert(11)


def merge_bsts(first_bst, second_bst):
    merged_bst = BST()

    def tree_to_sorted_list(root, sorted_list):
        if root is None:
            return
        tree_to_sorted_list(root.left, sorted_list)
        sorted_list.append(root.key)
        tree_to_sorted_list(root.right, sorted_list)

    def sorted_list_to_bst(sorted_list, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        merged_bst.insert(sorted_list[mid])
        sorted_list_to_bst(sorted_list, start, mid - 1)
        sorted_list_to_bst(sorted_list, mid + 1, end)
        return merged_bst

    # Convert both trees to sorted lists
    list1, list2 = [], []
    tree_to_sorted_list(first_bst.root, list1)
    tree_to_sorted_list(second_bst.root, list2)

    # Merge the sorted lists
    merged_list = sorted(list1 + list2)

    # Convert the merged list back into a balanced BST
    return sorted_list_to_bst(merged_list, 0, len(merged_list) - 1)

    # Verify the merged tree by doing an in-order traversal
    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print(node.key, end=" ")
            in_order_traversal(node.right)

    print("In-order traversal of the merged tree:")
    in_order_traversal(merged_tree)

def find_kth_smallest_element(tree, k):

    if tree is None:
        return None

    def which_smallest_number(tree):
        if tree is None:
            return 0
        return which_smallest_number(tree.left) + 1

    size = which_smallest_number(tree)

    if k == size:
        return tree.key
    elif k < size:
        return find_kth_smallest_element(tree.left, k)
    else:
        return find_kth_smallest_element(tree.right, k - size) # k - size because we already know that the left subtree has the number of size smaller elements


def balance_bst(tree):

    balance_bst = BST()

    def tree_to_sorted_list(root, sorted_list):
        if root is None:
            return
        tree_to_sorted_list(root.left, sorted_list)
        sorted_list.append(root.key)
        tree_to_sorted_list(root.right, sorted_list)

    def sorted_list_to_bst(sorted_list, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        balance_bst.insert(sorted_list[mid])
        tree.left = sorted_list_to_bst(sorted_list, start, mid - 1)
        tree.right = sorted_list_to_bst(sorted_list, mid + 1, end)
        return tree

    # Convert the tree to a sorted list
    sorted_list = []
    tree_to_sorted_list(tree.root, sorted_list)


    # Convert the sorted list back into a balanced BST
    return sorted_list_to_bst(sorted_list, 0, len(sorted_list) - 1)

def find_elements_in_range(tree, min_val, max_val):

    def find_elements_in_range_helper(node, min_val, max_val, result):
        if node is None:
            return

        if node.key > min_val:
            find_elements_in_range_helper(node.left, min_val, max_val, result)
        if min_val <= node.key <= max_val:
            result.append(node.key)
        if node.key < max_val:
            find_elements_in_range_helper(node.right, min_val, max_val, result)

    result = []
    find_elements_in_range_helper(tree, min_val, max_val, result)
    return result

print(merge_bsts(bst, bst2).inorder_traversal())
print(find_kth_smallest_element(bst.root, 3))
print(balance_bst(bst).inorder_traversal())
print(find_elements_in_range(bst.root, 2, 6))
