#!/usr/local/bin/python3
import random
from itertools import permutations
from string import ascii_lowercase
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(2)
    print('ab', 3)
    print("cab")
    print("fan")
    print("bat")
    print('a', 2)
    print("qwe")
    print("poke")
elif case_num == 1:
    print(4)
    print('ty', 2)
    print("tcaby")
    print("ybat")
    print('wa', 3)
    print("qwae")
    print("wat")
    print("wam")
    print('xyz', 1)
    print('zyxyzxzyyxzyzxzxy')
    print('asd', 1)
    print('das')
else:
    # output what should be read in as input by
    # contestant code
    test_case_count = random.randint(5, 10)
    print(test_case_count)
    for t in range(test_case_count):
        n = random.randint(1, 7)
        a_letters = "".join(random.sample(ascii_lowercase, k=n))
        word_count = random.randint(n, n*4)
        should_work = random.randint(0, 1) == 0
        perms_to_use = permutations(a_letters)
        words_to_show = []
        for w in range(word_count):
            garbage = [''.join(random.choices(ascii_lowercase, k=20)) for i in range(2)]
            if should_work:
                mid = ''
                try:
                    mid = list(next(perms_to_use))
                except:
                    mid = []
                mid = ''.join(mid)
                words_to_show.append(
                    garbage[0] + mid + garbage[1]
                )
            else:
                words_to_show.append(
                    garbage[0] + garbage[1] + 'z'*n
                )
        print(a_letters, word_count)
        for word in words_to_show:
            print(word)
                

            
        
