#!/usr/local/bin/python3
from random import randint, sample
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    lab = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(3,3)
    for row in lab:
        print(*row)
elif case_num == 1:
    lab = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
    print(3, 3)
    for row in lab:
        print(*row)
else:
    # output what should be read in as input by
    # contestant code
    m = randint(1, 200)
    n = randint(1, 200)
    stamina_limits = range(-1000, 1001)
    lab = [sample(stamina_limits, n) for _ in range(m)]
    print(m, n)
    for row in lab:
        print(*row)
