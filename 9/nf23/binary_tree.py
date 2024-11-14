from typing import Optional, Union

class TreeNode:
    def __init__(self, key: int) -> None:
        self.key: int = key
        # self.obj = obj
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None



def parse_tuple(data: Union[tuple, int, None]) -> Optional[TreeNode]:
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
        return node
    elif data is None:
        return None
    elif isinstance(data, int):
        return TreeNode(data)
    else:
        raise TypeError


def display_tree(node: Optional[TreeNode], space: str = "\t", level: int = 0) -> None:
    if not node:
        print(f"{space * level}∅")
        return

    if not node.left and not node.right:
        print(f"{space * level}{node.key}")
        return

    display_tree(node.right, space, level + 1)
    print(f"{space * level}{node.key}")
    display_tree(node.left, space, level + 1)

def tree_height(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    return 1 + max(tree_height(node.left), tree_height(node.right))

def tree_size(node: Optional[TreeNode]) -> int:
    if not node:
        return 0

    return 1 + tree_size(node.left) + tree_size(node.right)


if __name__ == '__main__':
    # (left_subtree, key {obj} , right_subtree)
    tree_tuple = ((1, 3, None), 2, ((None, 3, 6), 5, (6, 7, 8)))
    root = parse_tuple(tree_tuple)
    # print(root)
    # print(root.key) # 0
    # print(root.left.key, root.right.key) # 1
    # print(root.left.left.key, root.left.right, root.right.left.key, root.right.right.key) # 2
    display_tree(root)
    print(f"Tree height: {tree_height(root)}, Size: {tree_size(root)}")
