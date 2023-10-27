from collections import deque, defaultdict as dd
import sys
from functools import reduce
import time


def reduce_set(to_reduce):
    return reduce(lambda x, y : x | y, to_reduce, set())


def try_direction(start_y, start_x, _moves_remaining, 
                    position_to_number, number_to_positions):
    '''returns all spots reachable from (start_y, start_x)'''
    fringe = deque()
    start = (start_y, start_x)
    for spot in number_to_positions[position_to_number[start]]:
        fringe.append((*spot, [position_to_number[spot]], _moves_remaining.copy()))
    ret = set()
    while fringe:
        y, x, lands_seen, remaining_moves = fringe.pop()
        remaining_moves = remaining_moves.copy()
        if not len(remaining_moves):
            ret.add((y, x))
            continue
        dy, dx = remaining_moves.pop()
        new_spot = (y + dy, x + dx)
        if position_to_number[new_spot] == position_to_number[y, x]:
            new_spot = (y + dy*2, x + dx*2) 
        to_add = []
        for connected_spot in number_to_positions[position_to_number[new_spot]]:
            if position_to_number[connected_spot] not in lands_seen:
                to_add.append((*connected_spot, lands_seen + [position_to_number[connected_spot]], remaining_moves.copy()))
        fringe.extend(to_add)
    return ret

def show_board(grid, reachable_spots, start):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in reachable_spots or (y, x) == start:
                print(f"{'S' if (y, x) == start else '*'}{grid[y][x]}".rjust(3, '.'), end='.', file=sys.stderr)
            else:
                print(f"{grid[y][x]}".rjust(3, '.'), end='.', file=sys.stderr)
        print(file=sys.stderr)

def run_case():
    y_dim, x_dim, start_y, start_x = map(int, input().split())
    grid = [input() for _ in range(y_dim)]
    grid = [list(map(int, line.split())) for line in grid]

    number_to_positions = dd(set)
    position_to_number = dd(lambda: -7)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            number_to_positions[grid[y][x]].add((y, x))
            position_to_number[(y, x)] = grid[y][x]

    reachable_spots = set()
    start = (start_y, start_x)
    iteration = 0
    for y_dir, x_dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for x_amount, y_amount in [(2, 1), (1, 2)]:
            current_moves = [(1*x_dir, 0)] * x_amount + [(0, 1*y_dir)] * y_amount
            for ordering in range(2):
                iteration +=1 
                current_path = try_direction(*start, current_moves, 
                                position_to_number, number_to_positions)
                reachable_spots |= current_path
                current_moves = current_moves[::-1] 

    # show_board(grid, reachable_spots, start)


    unique_numbers = len({position_to_number[pos] for pos in reachable_spots})
    print(unique_numbers)

if __name__ == '__main__':
    cases = int(input())
    for t in range(cases):
        run_case()