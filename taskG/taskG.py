def to_bin(digit: int) -> str:
    if digit == 0:
        return "0"
    bin_num: str = ""
    c: int = digit

    while c > 0:
        if c % 2:
            bin_num += "1"
        else:
            bin_num += "0"
        c = int(c / 2)
    return bin_num[::-1]


def load_data() -> None:
    file = open("/run/media/greger/Disk_E/GRENOW/Dev/sprints/Algoritms/taskG/input.txt", "rt")
    data: int = int(file.read())
    print(to_bin(data))
    # print(bin(data)[2:])


if __name__ == '__main__':
    load_data()
    # import timeit
    # print(timeit.timeit("load_data()", number=1, setup="from __main__ import load_data"))
