from typing import List


def load_data() -> None:
    file = open("/run/media/greger/Disk_E/GRENOW/Dev/sprints/Algoritms/taskL/input.txt", "rt")
    data: List[List[int]] = [[*map(str, x)] for x in file.read().split()]
    data_1 = data[0]
    data_2 = data[1]

    difference_1 = set(data_1).difference(set(data_2))
    difference_2 = set(data_2).difference(set(data_1))
    print(difference_1, difference_2)
    for x in data_2:
        if x in data_1:
            data_2.remove(x)
    # print(data_2)


if __name__ == '__main__':
    load_data()
    # import timeit
    # print(timeit.timeit("load_data()", number=1, setup="from __main__ import load_data"))
