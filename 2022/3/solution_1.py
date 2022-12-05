from functools import reduce as r
from string import ascii_letters as p

def solve():
    with open('input.txt', 'r') as f:

        # 130 characters
        return r(lambda x, y: x + p.find(set(y[:len(y)//2]).intersection((set(y[len(y)//2:len(y)]))).pop()) + 1, f.read().splitlines(), 0)

if __name__ == "__main__":
    print(solve())
