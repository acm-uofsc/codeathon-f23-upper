import re
from collections import defaultdict
import sys
# y change, followed by x change, 
# up being negative y, left is negative x
move_to_offset = {
    "NW": (-.5, -1),
    "N": (-1, 0),
    "NE": (-.5, 1),
    "SE": (.5, 1),
    "S": (1, 0),
    "SW": (.5, -1),
}

def run_test_case():
    n, a = input().split() 
    n = int(n)
    matches = re.findall(r'NW|NE|SE|SW|N|S', a)
    assert ''.join(matches) == a
    seen = defaultdict(int)
    pos_y = 0
    pos_x = 0
    seen[pos_y, pos_x] += 1
    for match in matches:
        dy, dx = move_to_offset[match]
        pos_y += dy
        pos_x += dx
        seen[pos_y, pos_x] += 1
    num_been_to_more_than_once = sum(1 for x in seen if seen[x] > 1) 
    if num_been_to_more_than_once > 0 and num_been_to_more_than_once % n == 0:
        print("yes", num_been_to_more_than_once)
    else:
        print("no")
    

cases = int(input())
for t in range(cases):
    run_test_case()
        