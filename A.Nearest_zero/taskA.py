# 85057742
from collections.abc import Iterable
from itertools import chain
from typing import List


def pattern(itr: Iterable) -> List[int]:
    return [int(x) for x in itr]


def nearest_zeros(array: List[int], len_street: int) -> List[int]:
    zero_list: List[int] = []
    length: int = 0
    len_street -= 1
    for i, x in enumerate(array):
        if x == 0 and i == 0:
            zero_list.append(x)
            length = 0
            continue
        length += 1
        if x == 0:
            if length != 1:
                zero_list.append(length - 1)
            zero_list.append(0)
            length = 0
        if i == len_street:
            zero_list.append(length + 1)

    answer: List[int] = []
    len_zeros: int = len(zero_list)
    for i, x in enumerate(zero_list):
        if x == 0:
            answer.append(x)
        elif i == 0 and x != 0:
            itr = range(x, 0, -1)
            answer += pattern(itr)
        elif i == len_zeros - 1:
            itr = range(1, x)
            answer += pattern(itr)
        elif i != len_zeros:
            hav_len = x // 2
            merge_itr = chain(range(1, 1 + hav_len), range(x - hav_len, 0, -1))
            answer += pattern(merge_itr)
    return answer


def load_data() -> None:
    file = open("./input.txt", "rt")
    data = []
    for a in file.read().split("\n"):
        data.append(list(map(int, a.split())) if not a.isdigit() else int(a))
    len_street: int = data[0]
    arr: List = [data[1]] if isinstance(data[1], int) else data[1]
    print_path(nearest_zeros(arr, len_street))


def print_path(arr: List[int]) -> None:
    # In this way speed up as opposed of "*arr"
    # print(" ".join(map(str, arr)))
    print(*arr)


if __name__ == "__main__":
    load_data()
