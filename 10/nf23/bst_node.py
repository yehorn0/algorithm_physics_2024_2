from typing import Generic, TypeVar, Optional


T = TypeVar('T')


class BSTNode(Generic[T]):
    def __init__(self, _object: T) -> None:
        self.key: str = _object.key
        self.__object: T = _object

        self.left: Optional["BSTNode"] = None
        self.right: Optional["BSTNode"] = None

    @property
    def object_(self) -> T:
        return self.__object


def display(
        node: BSTNode[T],
        space: str = "\t",
        level: int = 0
) -> None:
    if not node:
        print(f"{space * level}∅")
        return

    if not node.left and not node.right:
        print(f"{space * level}{node.key}")
        return

    display(node.right, space, level + 1)
    print(f"{space * level}{node.key}")
    display(node.left, space, level + 1)


def insert(node: BSTNode[T] | None, _object: T) -> BSTNode[T] | None:
    if not node:
        node = BSTNode[T](_object)
    elif _object.key < node.key:
        node.left = insert(node.left, _object)
    elif _object.key > node.key:
        node.right = insert(node.right, _object)
    else:
        raise ValueError("Identical keys are not allowed")

    return node


def find(node: BSTNode[T] | None, key: str) -> BSTNode[T] | None:
    if node is None:
        raise KeyError(key)

    if node.key == key:
        return node
    elif node.key > key:
        return find(node.left, key)
    else:
        return find(node.right, key)


def update(node: BSTNode[T] | None, _object: T) -> None:
    target = find(node, _object.key)
    target.object_.update(_object)


def list_all(node: BSTNode[T] | None) -> list[T]:
    if not node:
        return []

    return list_all(node.left) + [node.object_] + list_all(node.right)
    # return [node.object_] + list_all(node.left) +  list_all(node.right) preorder
    # return list_all(node.left) + list_all(node.right) + [node.object_] postorder

def tree_size(node: BSTNode[T] | None) -> int:
    if not node:
        return 0

    return 1 + tree_size(node.left) + tree_size(node.right)


if __name__ == '__main__':
    from user import User

    user0 = User("user0", "User 0", email="user0@example.com")
    user1 = User("user1", "User 1", email="user1@example.com")
    user2 = User("user2", "User 2", email="user2@example.com")
    user3 = User("user3", "User 3", email="user3@example.com")

    tree = BSTNode[User](user0)
    insert(tree, user1)
    insert(tree, user2)
    insert(tree, user3)

    display(tree)

    user = find(tree, "user1")
    print(user)
    user3_new = User("user3", "User 3 new", email="user3new@example.com")

    update(tree, user3_new)
    u3_found = find(tree, "user3")
    print(u3_found)

    try:
        find(tree, "user_not_found")
    except KeyError:
        print("KeyError")

    display(tree)
    print(list_all(tree))



