from AoCLibrary import *
with open("input14.txt") as f:
    real_input = f.read()

import time

ROLLING_ROCK = 'O'
OPEN_SPACE = '.'
WALL = '#'
def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    board = to_board(a)
    return run_cycles(board, 1000000000)

def run_cycles(board, cycles_to_run: int):
    seen = dd(list)
    time_to_load = {}
    repeats_every_n = None
    for c in range(cycles_to_run):
        if c % 100 == 0:
            print(c)
        for direction in range(4):
            board = roll_north(board)
            board = rotate90(board)
        fingerprint = board_to_string(board)
        current_load = get_load(board)
        if fingerprint in seen:
            if repeats_every_n is None:
                repeats_every_n = c - seen[fingerprint][-1][0]
                loop_start = seen[fingerprint][-1][0]
            else:
                assert time_to_load[c - repeats_every_n] == current_load
        seen[fingerprint].append((c, current_load))
        time_to_load[c] = current_load
        if repeats_every_n is not None:
            return time_to_load[((cycles_to_run - loop_start) % repeats_every_n) + loop_start - 1]


def roll_north(starting_board):
    board = deepcopy(starting_board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == ROLLING_ROCK:
                board[y][x] = OPEN_SPACE
                roll_y = y
                roll_x = x
                while board[roll_y][roll_x] == OPEN_SPACE:
                    roll_y -= 1
                    if roll_y < 0:
                        break
                roll_y += 1
                board[roll_y][roll_x] = ROLLING_ROCK
    return board
    
def get_load(board):
    ret = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == ROLLING_ROCK:
                ret += len(board) - y
    return ret





samp = r"""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....

""".lstrip("\n")

if samp and "r" not in sys.argv:
    sample_answer = main(samp)
    print("sample", sample_answer)
else:
    print("no sample provided")

if "s" in sys.argv:
    exit()
result = main(real_input)
if result is not None:
    ans(result)