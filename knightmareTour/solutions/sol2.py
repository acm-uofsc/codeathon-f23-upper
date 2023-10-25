from collections import deque, defaultdict as dd
import sys
from functools import reduce
import time


def reduce_set(to_reduce):
    return reduce(lambda x, y : x | y, to_reduce, set())


def try_direction(start_y, start_x, _moves_remaining):
    '''returns all spots reachable from (start_y, start_x)'''
    # print("_moves_remaining", _moves_remaining)
    fringe = deque()
    start = (start_y, start_x)
    # print("number_to_positions[position_to_number[start]]", number_to_positions[position_to_number[start]])
    for spot in number_to_positions[position_to_number[start]]:
        fringe.append((*spot, [position_to_number[spot]], _moves_remaining.copy()))
    # print("fringe")
    # for f in fringe:
    #     print(f)
    # print("end fringe")
    ret = set()
    while fringe:
        # print("fringe[0]", fringe[0])
        y, x, lands_seen, remaining_moves = fringe.pop()
        remaining_moves = remaining_moves.copy()
        if not len(remaining_moves):
            # print("land_seen", lands_seen)
            ret.add((y, x))
            # if position_to_number[(y, x)] == 36:
            #     print("got to this pos with seeing", lands_seen)
            continue
        dy, dx = remaining_moves.pop()
        new_spot = (y + dy, x + dx)
        # TODO: if changed to not use knights moves, use a while loop
        if position_to_number[new_spot] == position_to_number[y, x]:
            new_spot = (y + dy*2, x + dx*2) 
            # print("slid from", (y, x), "to", new_spot)
            # fringe.append((*connected_spot, lands_seen + [position_to_number[connected_spot]], remaining_moves.copy()))
        to_add = []
        for connected_spot in number_to_positions[position_to_number[new_spot]]:
            if position_to_number[connected_spot] not in lands_seen:
                to_add.append((*connected_spot, lands_seen + [position_to_number[connected_spot]], remaining_moves.copy()))
            # else:
                # assert False
        # print("just added")
        # for x in to_add:
        #     print(x)
        fringe.extend(to_add)
        # show_board(reduce_set([number_to_positions[land] for land in lands_seen]))
        # exit()
        # print("lands_seen", lands_seen)
        # time.sleep(1)
    # print("ret", ret)
    return ret

def show_board(reachable_spots):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in reachable_spots or (y, x) == start:
                print(f"{'S' if (y, x) == start else '*'}{grid[y][x]}".rjust(3, '.'), end='.', file=sys.stderr)
            else:
                print(f"{grid[y][x]}".rjust(3, '.'), end='.', file=sys.stderr)
        print(file=sys.stderr)

y_dim, x_dim, start_y, start_x, moves_to_make = map(int, input().split())
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
            current_path = try_direction(*start, current_moves)
            reachable_spots |= current_path
            current_moves = current_moves[::-1] 

show_board(reachable_spots)
# for spot in reachable_spots:
#     print(*spot)

unique_numbers = len({position_to_number[pos] for pos in reachable_spots})
print(unique_numbers)

