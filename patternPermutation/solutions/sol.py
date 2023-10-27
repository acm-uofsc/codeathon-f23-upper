import re
from itertools import permutations as perms

def search_for_perm(perm, words) -> bool:
    '''returns True if the permutation
    was found in the list of words'''
    for word in words:
        if perm in word:
            return True
    return False

def run_test_case():
    a, n = input().split() 
    n = int(n)
    words = [input() for _ in range(n)]
    for perm in perms(a):
        found = search_for_perm(''.join(perm), words)
        if not found:
            print('no')
            return
    print('yes')

cases = int(input())
for t in range(cases):
    run_test_case()
        