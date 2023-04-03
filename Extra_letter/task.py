from typing import List


def load_data() -> None:
    file = open("./input.txt", "rt")
    data: List[str] = file.read().split()
    str1 = data[0]
    str2 = data[1]

    for i in range(len(str2)):
        last = str2[i]
        if last in str1:
            str1 = str1.replace(last, '', 1)
        else:
            print(last)
            break


if __name__ == "__main__":
    load_data()
