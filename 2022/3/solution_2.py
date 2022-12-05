from functools import reduce as r
from string import ascii_letters as p


def solve():
    with open('input.txt', 'r') as f:

        # 174 chars
        l = f.read().splitlines()
        return r(lambda x, y: x + p.find(set(y[0]).intersection(set(y[1])).intersection(set(y[2])).pop()) + 1, [l[i: i + 3] for i in range(0, len(l), 3)], 0)


if __name__ == "__main__":
    print(solve())
