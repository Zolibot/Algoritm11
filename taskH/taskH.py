from typing import List


def sum_bin(num_1: List[int], num_2: List[int]) -> str:
    carry = 0
    answer = []
    max_len = max(len(num_1), len(num_2))
    num_1 += (max_len - len(num_1)) * [0]
    num_2 += (max_len - len(num_2)) * [0]

    for digit in zip(num_1, num_2):
        value = digit[0] + digit[1] + carry
        carry = value // 2
        answer.append(value % 2)
    if carry == 1:
        answer.append(1)

    return ''.join(map(str, answer[::-1]))


def load_data() -> None:
    file = open("/run/media/greger/Disk_E/GRENOW/Dev/sprints/Algoritms/taskH/input.txt", "rt")
    data: List[List[int]] = [[*map(int, x)][::-1] for x in file.read().split()]
    print(sum_bin(*data))


if __name__ == '__main__':
    load_data()
    # import timeit
    # print(timeit.timeit("load_data()", number=1, setup="from __main__ import load_data"))
