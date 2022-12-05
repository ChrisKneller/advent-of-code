from functools import reduce as r
from string import ascii_letters as p

def solve():
    with open('input.txt', 'r') as f:

        # 119 characters
        return r(lambda x, y: x + p.find(set(y[:(l:=len(y)//2)]).intersection((set(y[l:len(y)]))).pop()) + 1, f.readlines(), 0)

if __name__ == "__main__":
    print(solve())
