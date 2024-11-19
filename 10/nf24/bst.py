from tree_node import TreeNode

def is_bst(node: TreeNode | None) -> bool:
    if node is None:
        return True

    is_bst_left = is_bst(node.left)
    is_bst_right = is_bst(node.right)

    # left_key = node.left.key if node.left else None
    is_left_key_valid = node.left.key < node.key if node.left else True

    # right_key = node.left.key if node.left else None
    is_right_key_valid = node.right.key > node.key if node.right else True

    is_bst_node = all([
        is_bst_left, is_bst_right, is_left_key_valid, is_right_key_valid
    ])

    return is_bst_node


if __name__ == '__main__':
    non_bst_tuple = ((1, 3, None), 2, ((None, 3, 6), 5, (6, 7, 8)))
    non_bst_tree_root = TreeNode.create_tree(non_bst_tuple)
    assert not is_bst(non_bst_tree_root)

    bst_tuple = ((1, 2, None), 3, ((None, 6, 7), 10, (12, 14, 290)))
    bst_tree_root = TreeNode.create_tree(bst_tuple)
    assert  is_bst(bst_tree_root)
