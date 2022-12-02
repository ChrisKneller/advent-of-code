```shell
> python3 solution_1.py
12772

> python3 solution_2.py
11618

> python -m timeit -s "from solution_1 import solve" "solve()"
200 loops, best of 5: 944 usec per loop

> python -m timeit -s "from solution_2 import solve" "solve()"
200 loops, best of 5: 896 usec per loop
```
