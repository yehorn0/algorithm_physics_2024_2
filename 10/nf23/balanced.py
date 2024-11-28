import math
from bst_node import BSTNode, T


def is_balanced(node: BSTNode[T] | None) -> tuple[bool, int]:
    if not node:
        return True, 0

    is_left_balanced, left_height = is_balanced(node.left)
    is_right_balanced, right_height = is_balanced(node.right)

    balanced = is_right_balanced and is_left_balanced and abs(left_height - right_height) <= 1
    height = 1 + max(left_height, right_height)

    return balanced, height


def make_balanced(_objects: list[T], low: int = 0, high: int = -math.inf) -> BSTNode[T] | None:
    if high == -math.inf:
        high = len(_objects) - 1

    if low > high:
        return None

    mid = (low + high) // 2
    object_to_insert = _objects[mid]

    root = BSTNode[T](object_to_insert)
    root.left = make_balanced(_objects, low, mid - 1)
    root.right = make_balanced(_objects, mid + 1, high)

    return root


if __name__ == '__main__':
    from user import User
    from bst_node import insert, display, list_all

    user0 = User("user0", "User 0", email="user0@example.com")
    user1 = User("user1", "User 1", email="user1@example.com")
    user2 = User("user2", "User 2", email="user2@example.com")
    user3 = User("user3", "User 3", email="user3@example.com")

    tree = BSTNode[User](user0)
    insert(tree, user1)
    insert(tree, user2)
    insert(tree, user3)

    display(tree)
    print(is_balanced(tree))

    balanced_tree = make_balanced(list_all(tree))
    display(balanced_tree)
    print(is_balanced(balanced_tree))


