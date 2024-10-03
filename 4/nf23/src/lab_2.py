"""
[43, 51, 35, 4]
43--51--35--4
    ^
Left: 43*1 = 43
Right: 35*1 + 4*2 = 35 + 8 = 43
Return: 1

If no equilibrium index, then return -1

[6, 6, 9] -> -1

Help functions with list:
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 10]

sum(number_list)
sum(number * idx for number, idx in enumerate(number_list[0:current_idx])) [current_idx+1:]

max(number_list)
min(number_list)
"""

def weights_equilibrium(weights: list[int]) -> int:
    for current_idx in range(len(weights)):
        left = sum(
            weight * (current_idx - idx) for idx, weight in enumerate(weights[:current_idx])
        )

        # left = 0
        # for idx, weight in enumerate(weights[:current_idx]):
        #     left += weight * (current_idx - idx)

        right = sum(
            weight * (idx + 1) for idx, weight in enumerate(weights[current_idx + 1:])
        )
        # right = 0
        # for idx, weight in enumerate(weights[current_idx + 1:]):
        #     right += weight * (idx + 1)
        if left == right:
            return current_idx

    return -1