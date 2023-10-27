from collections import deque, defaultdict as dd
import sys
from functools import reduce


def try_direction(start_y, start_x, y_dir, x_dir, y_amount, x_amount):
    fringe = deque([(start_y, start_x, [(start_y, start_x)], set(), y_amount, x_amount, '')])
    ret = set()
    while fringe:
        y, x, poses_seen, lands_seen, y_rem, x_rem, prev = fringe.popleft()
        if len(poses_seen) == 4:
            ret.add((y, x))
            continue
        if y + y_dir in range(len(grid)) and y_rem > 0 and (prev in ['', 'y'] or (prev == 'x' and x_rem == 0)) and grid[y + y_dir][x] not in lands_seen:
            for new_pos in number_to_positions[grid[y + y_dir][x]]:
                if new_pos not in poses_seen:
                    fringe.append((*new_pos, poses_seen + [new_pos], lands_seen | {position_to_number[y+y_dir, x]}, y_rem - 1, x_rem, 'y'))
        if x + x_dir in range(len(grid[0])) and x_rem > 0 and (prev in ['', 'x'] or (prev == 'y' and y_rem == 0)) and grid[y][x + x_dir] not in lands_seen:
            for new_pos in number_to_positions[grid[y][x + x_dir]]:
                if new_pos not in poses_seen:
                    fringe.append((*new_pos, poses_seen + [new_pos], lands_seen | {position_to_number[y, x + x_dir]}, y_rem, x_rem - 1, 'x'))
    print(ret)
    return ret


y_dim, x_dim, start_y, start_x, moves_to_make = map(int, input().split())
grid = [input() for _ in range(y_dim)]
grid = [list(map(int, line.split())) for line in grid]

number_to_positions = dd(set)
position_to_number = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        number_to_positions[grid[y][x]].add((y, x))
        position_to_number[(y, x)] = grid[y][x]


reachable_spots = []
start = (start_y, start_x)
for y_dir, x_dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
    for x_amount, y_amount in [(2, 1), (1, 2)]:
        reachable_spots.append(try_direction(*start, y_dir, x_dir, y_amount, x_amount))
reachable_spots = reduce(lambda x, y : x | y, reachable_spots, set())

# print(reachable_spots, file=sys.stderr)
unique_numbers = len({position_to_number[pos] for pos in reachable_spots})

print(unique_numbers)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (y, x) in reachable_spots or (y, x) == start:
            print(f"{'S' if (y, x) == start else '*'}{grid[y][x]}".rjust(3, '.'), end='.', file=sys.stderr)
        else:
            print(f"{grid[y][x]}".rjust(3, '.'), end='.', file=sys.stderr)
    print(file=sys.stderr)
