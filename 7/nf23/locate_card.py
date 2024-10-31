def locate_card_linear(cards: list[int], query: int) -> int: # O(n)
    for idx, card in enumerate(cards):
        if card == query:
            return idx

    return -1


def locate_card(cards: list[int], query: int) -> int:
    left, right = 0, len(cards) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_card = cards[mid]

        if mid_card == query:
            if mid >= 1 and cards[mid - 1] == query:
                right = mid - 1
            else:
                return mid
        elif mid_card < query:
            right = mid - 1
        else:
            left = mid + 1

    return -1

"""
13, 12, 11, 7, 5, 3, 1, 0; len = 8; mid = 4
query: 11
left = 0
right = len(cards) - 1; mid = (right + left) // 2
mid = 4; mid_elem = cards[mid] = 5

11 < mid => right = mid; mid = (right + left) // 2 = 2; mid_elem = 11
=========================
1: N
2: N/2
3: N/4 = N/ 2^2
....
k: N/2^k = 1
2^k = N
k = log2N
O(log2N) = C*O(logN)
log2N = logaN / loga2
"""

if __name__ == '__main__':
    result = locate_card(
        [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        6
    )

    result_linear = locate_card_linear(
        [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        6
    )

    print(result, result_linear)