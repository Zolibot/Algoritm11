def max_word(words):
    index = []
    for w in words:
        index.append(len(w))

    max_index = index.index(max(index))
    max_len = index[max_index]
    return words[max_index], max_len


def load_data() -> None:
    file = open("taskE/input.txt", "rt")
    data = file.read()
    data = data.strip().split("\n")
    max_w, max_index = max_word(data[1].split())
    print(max_w)
    print(max_index)


if __name__ == '__main__':
    load_data()
    # import timeit
    # print(timeit.timeit("load_data()", number=1, setup="from __main__ import load_data"))
