# 84981822
from typing import List
from itertools import chain


def pattern3(i: int) -> List[int]:
    data: List[int] = []
    for j in range(i, 0, -1):
        data.append(j)
    return data


def pattern2(i: int) -> List[int]:
    data: List[int] = []
    for j in range(1, i):
        data.append(j)
    return data


def pattern(i: int) -> List[int]:
    data: List[int] = []
    hav_len = i // 2
    itr = chain(range(1, 1 + hav_len), range(i - hav_len, 0, -1))
    for x in itr:
        data.append(x)
    return data


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
            answer += pattern3(x)
        elif i == len_zeros - 1:
            answer += pattern2(x)
        elif i != len_zeros:
            answer += pattern(x)
    return answer


def load_data() -> None:
    file = open("./input.txt", "rt")
    data = [list(map(int, a.split())) if not a.isdigit() else int(a) for a in file.read().split("\n")]
    len_street: int = data[0]  # type: ignore
    arr: List[int] = [data[1]] if isinstance(data[1], int) else data[1]  # type: ignore
    print_path(nearest_zeros(arr, len_street))


def print_path(arr: List[int]) -> None:
    print(" ".join(map(str, arr)))


if __name__ == '__main__':
    load_data()
    # import timeit
    #
    # print(timeit.timeit("load_data()", number=1, setup="from task import load_data"))
