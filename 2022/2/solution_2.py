from functools import reduce as r


def solve():
    with open('input.txt', 'r') as f:

        # 148 characters
        return r((lambda x, y: x + {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}[y]), f.read().splitlines(), 0)


if __name__ == "__main__":
    print(solve())
