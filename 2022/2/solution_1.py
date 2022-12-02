from itertools import accumulate as a


def solve():
    with open('input.txt', 'r') as f:

        # 161 characters
        return max(a(f.read().splitlines(), (lambda x, y: x + {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}[y]), initial=0))


if __name__ == "__main__":
    print(solve())
