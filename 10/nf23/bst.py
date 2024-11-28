from tree_node import TreeNode


def is_bst(node: TreeNode | None) -> bool:
    if node is None:
        return True

    is_bst_left = is_bst(node.left)
    is_bst_right = is_bst(node.right)

    # left_key = node.left.key if node.left else None
    # is_left_key_valid = left_key < node.key if left_key is not None else True
    is_left_key_valid = node.left.key < node.key if node.left else True

    # right_key = node.right.key if node.right else None
    # is_right_key_valid = right_key > node.key if right_key is not None else True
    is_right_key_valid = node.right.key > node.key if node.right else True

    is_bst_node = all([
        is_bst_left, is_bst_right,
        is_left_key_valid, is_right_key_valid
    ])

    return is_bst_node


if __name__ == '__main__':
    # (left_subtree, key {obj} , right_subtree)
    tree_tuple = ((1, 3, None), 2, ((None, 3, 6), 5, (6, 7, 8)))
    root = TreeNode.create_tree(tree_tuple)

    print(is_bst(root))

    bst_tuple = ((1, 2, None), 3, ((None, 6 , 7), 10, (11, 14, 20)))
    bst_root = TreeNode.create_tree(bst_tuple)
    print(is_bst(bst_root))
