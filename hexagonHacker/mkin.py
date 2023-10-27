#!/usr/local/bin/python3
import random
from itertools import permutations
from string import ascii_lowercase
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(4)
    print(2, 'NSNENSNSNW')
    print(2, 'NSNENSNS')
    print(2, 'NNNN')
    print(3, 'NSNSNS')
elif case_num == 1:
    print(2)
    print(1, 'NS')
    print(4, 'NESESSWNWNSNSNSNSNSNS')
else:
    # output what should be read in as input by
    # contestant code
    test_case_count = random.randint(10, 20)
    hard_case_cutoff = 7
    if case_num > hard_case_cutoff:
        test_case_count = random.randint(5, 10)
    print(test_case_count)
    for t in range(test_case_count):
        n = random.randint(2,5)
        path_len = random.randint(1, 20) * 10
        if case_num > hard_case_cutoff and t == 0:
            path_len = 100_000
        path_taken = random.choices(["NW","N","NE","SE","S","SW"], k=path_len)
        print(n, ''.join(path_taken))

        
        
        
    
