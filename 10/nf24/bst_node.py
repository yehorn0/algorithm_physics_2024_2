import math
from typing import Optional, Any


class BSTNode:
    def __init__(self, _object: Any) -> None:
        self.key: str = _object.key
        self.__object: Any = _object
        self.left: Optional["BSTNode"] = None
        self.right: Optional["BSTNode"] = None

    @property
    def object(self):
        return self.__object

    def display(
            self,
            space: str = "\t",
            level: int = 0
    ) -> None:
        if not self:
            print(f"{space * level}∅")
            return

        if not self.left and not self.right:
            print(f"{space * level}{self.key}")
            return

        BSTNode.display(self.right, space, level + 1)
        print(f"{space * level}{self.key}")
        BSTNode.display(self.left, space, level + 1)


def insert(node: BSTNode | None, _object: Any) -> BSTNode | None:
    if not node:
        node = BSTNode(_object)
    elif _object.key < node.key:
        node.left = insert(node.left, _object)
    elif _object.key > node.key:
        node.right = insert(node.right, _object)
    return node


def find(node: BSTNode | None, key: str) -> BSTNode | None:
    if node is None:
        raise KeyError

    if key == node.key:
        return node
    elif key < node.key:
        return find(node.left, key)
    else: # key > node.key
        return find(node.right, key)


def update(node: BSTNode | None, key: str, _object: Any) -> None:
    target = find(node, key)

    if target:
        target.object.update(_object)
        return

    raise KeyError


def inorder_traversal(node: BSTNode | None) -> list[Any]:
    if not node:
        return []

    return inorder_traversal(node.left) + [node.object] + inorder_traversal(node.right)


def is_balanced(node: BSTNode | None) -> tuple[bool, int]:
    if not node:
        return True, 0

    is_left_balanced, left_height = is_balanced(node.left)
    is_right_balanced, right_height = is_balanced(node.right)

    balanced = is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1
    height = 1 + max(left_height, right_height)

    return balanced, height


def make_balanced(_objects: list[Any], lo: int = 0, hi: int = -math.inf) -> BSTNode | None:
    # if not hi: :)))
    if hi == -math.inf:
        hi = len(_objects) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    obj = _objects[mid]

    root = BSTNode(obj)
    root.left = make_balanced(_objects, lo, mid - 1)
    root.right = make_balanced(_objects, mid + 1, hi)

    return root


def balance_bst(node: BSTNode) -> BSTNode:
    return make_balanced(inorder_traversal(node))


def tree_size(node: BSTNode | None) -> int:
    if not node:
        return 0

    return tree_size(node.left) + 1 + tree_size(node.right)


if __name__ == '__main__':
    from user import User  # import for checking functionality
    user0 = User("user0", "User 0", email="user0@example.com")
    user1 = User("user1", "User 1", email="user1@example.com")
    user2 = User("user2", "User 2", email="user2@example.com")
    user3 = User("user3", "User 3", email="user3@example.com")


    tree = insert(None, user0)
    insert(tree, user1)
    insert(tree, user2)
    insert(tree, user3)
    #tree.left = BSTNode(user1)
    #tree.right = BSTNode(user2)

    tree.display()

    # update(tree, "user1",
    #           User("user1", "New Name", "new_email@example.com"))
    # print(find(tree, "user1").object)

    print(inorder_traversal(tree))
    print(is_balanced(tree))

    # balanced = insert(None, user1)
    # insert(balanced, user0)
    # insert(balanced, user2)
    # balanced.display()
    # print(is_balanced(balanced))
    elems = inorder_traversal(tree)

    balanced = make_balanced(elems)
    balanced.display()
    print(is_balanced(balanced))
