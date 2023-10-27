#!/usr/local/bin/python3
import random
from itertools import permutations
from string import ascii_lowercase
from collections import defaultdict as dd

def print_board(grid, y_dim, x_dim, answer=None, start=(-1, -1)):
    if answer is None:
        answer = []
    filler = ' '
    fill_len = 2
    for y in range(y_dim):
        for x in range(x_dim):
            if (y, x) in answer or (y, x) == start:
                print(f"{'S' if (y, x) == start else '*'}{grid[y, x]}".rjust(fill_len, filler), end=filler)
            else:
                print(f"{grid[y, x]}".rjust(fill_len, filler), end=filler)
        print()

def generate_board(y_dim, x_dim, mode_lo=0, mode_hi=3):
    board = dd(int)
    cur_tile_num = 0
    # 0 is 4 same tiles
    # 1 is verticals
    # 2 is horizontals
    # 3 is 4 different tiles
    for y in range(0, y_dim, 2):
        for x in range(0, x_dim, 2):
            mode = random.randint(mode_lo, mode_hi)
            if mode == 0:
                for dy in range(2):
                    for dx in range(2):
                        board[y + dy, x + dx] = cur_tile_num
                cur_tile_num += 1
            elif mode == 1:
                for dx in range(2):
                    for dy in range(2):
                        board[y + dy, x + dx] = cur_tile_num
                    cur_tile_num += 1

            elif mode == 2:
                for dy in range(2):
                    for dx in range(2):
                        board[y + dy, x + dx] = cur_tile_num
                    cur_tile_num += 1

            elif mode == 3:
                for dy in range(2):
                    for dx in range(2):
                        board[y + dy, x + dx] = cur_tile_num
                        cur_tile_num += 1
    return board

case_num = int(input())
random.seed(case_num)
# 0 and 1 are the sample cases
if case_num == 0:
    print(1)
    y_dim, x_dim = 8, 8
    print(y_dim, x_dim, 4, 4)
    board=generate_board(y_dim, x_dim, 3, 3)
    print_board(board, y_dim, x_dim)
elif case_num == 1:
    print(2)
    y_dim, x_dim = 10, 10
    print(y_dim, x_dim, 4, 4)
    board=generate_board(y_dim, x_dim, 3, 3)
    for dy in range(2):
        for dx in range(2):
            board[4 + dy, 4 + dx] = 48
    print_board(board, y_dim, x_dim)
    
    y_dim, x_dim = 12, 8
    print(y_dim, x_dim, 6, 4)
    board=generate_board(y_dim, x_dim, 0, 3)
    print_board(board, y_dim, x_dim)

elif case_num == 2:
    print(1)
    y_dim, x_dim = 10, 10
    print(y_dim, x_dim, 4, 4)
    board=generate_board(y_dim, x_dim, 0, 3)
    print_board(board, y_dim, x_dim)

else:
    # output what should be read in as input by
    # contestant code
    case_count = random.randint(5, 10)
    print(case_count)
    for i in range(case_count):
        y_dim = random.randint(2,5) * 2
        x_dim = random.randint(2,5) * 2
        start_y = random.randint(0, y_dim - 1)
        start_x = random.randint(0, x_dim - 1)

        print(y_dim, x_dim, start_y, start_x)
        move_count = random.randint(1, 4)

        board = generate_board(y_dim, x_dim)
        print_board(board, y_dim, x_dim)

        
        
        
    
