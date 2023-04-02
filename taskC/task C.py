MATRIX = []


def check_index(x, y, row, colm):
    if row > x >= 0 and colm > y >= 0:
        if row == 1:
            return MATRIX[0][y]
        if colm == 1:
            return MATRIX[x]
        return MATRIX[x][y]


def neighbors(x, y, row, colm):
    direction = ((0, -1), (1, 0), (0, 1), (-1, 0))
    f = []
    for i, j in direction:
        dx = x + i
        dy = y + j
        tmp = check_index(dx, dy, row, colm)
        if tmp is not None:
            f.append(tmp)
    f.sort()
    return f


def load_data():
    file = open("../taskD/input.txt", "rt")
    data = file.read()
    data = [int(a) if a.isdigit() else list(map(int, a.split())) for a in data.split("\n")]

    row = data[0]
    colm = data[1]

    x = data[row + 2]
    y = data[row + 3]

    for num in range(row):
        MATRIX.append(data[2 + num])
    file.close()
    print(" ".join(map(str, neighbors(x, y, row, colm))))


if __name__ == "__main__":
    load_data()
