```shell
> python3 solution_1.py
67658

> python3 solution_2.py
200158

> python3 -m timeit -s 'from solution_1 import solve' 'solve()'
500 loops, best of 5: 531 usec per loop

> python3 -m timeit -s 'from solution_2 import solve' 'solve()'
500 loops, best of 5: 821 usec per loop
```
