from typing import Self, Any

class TreeNode:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Self | None = None
        self.right: Self | None = None


def parse_data(
    data: Any
) -> TreeNode | None:
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_data(data[0])
        node.right = parse_data(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + '∅')
        return

        # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


if __name__ == '__main__':
    tree2 = parse_data(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    display_keys(tree2)
