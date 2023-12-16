import re
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, ascii_letters as letters, digits
import string
all_letters = letters
import string
vowels_lower = "AEUIO".lower()
vowels = vowels_lower
import os
import sys
from sys import exit
from itertools import *
from more_itertools import *
import itertools
it = itertools
# import itertools as it
from math import ceil, exp, floor, gcd, factorial, inf, lcm
import math
# math.
import operator as op
from collections import *
from collections import defaultdict as dd
from functools import reduce, partial, lru_cache, cache, cmp_to_key
from copy import deepcopy
import hashlib
import heapq
from typing import NamedTuple, Type, List, Set
from dataclasses import dataclass
from enum import Enum
import bisect
# from numpy import sign
# get_sign = sign
# copysign = sign
# first_true()

import more_itertools
mi = more_itertools
# print(sys.version)
# more_itertools.

DEBUG = False
try:
#     # import networkx as nx
    from sympy.ntheory.modular import crt
    chinese = crt
except:
    pass

gcf = gcd
# to_exclude = ["pow"]
# for name in to_exclude:
producti = itertools.product
iproduct = itertools.product
iterproduct = itertools.product
iter_product = itertools.product
# acc = accumulate
l = list
groupby_and_size = run_length.encode
groupby_with_size = run_length.encode
#     del globals()[name]

using_pypy = False
try:
    import pyperclip
except ModuleNotFoundError:
    using_pypy = True

# sourcery skip: de-morgan
directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "^": (-1, 0),
    "V": (1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}
class Directions(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)
    LEFT = WEST
    RIGHT = EAST
    @staticmethod
    def opposite(to_get_opposite_of):
        opposite = {
            Directions.NORTH : Directions.SOUTH,
            Directions.EAST : Directions.WEST,
            Directions.SOUTH : Directions.NORTH,
            Directions.WEST : Directions.EAST,
        }

        return opposite[to_get_opposite_of]

SIDE_DIRS = (Directions.EAST, Directions.WEST)
LEFT_RIGHT_DIRS = SIDE_DIRS
UP_DOWN_DIRS = (Directions.NORTH, Directions.SOUTH)
TOP_DOWN_DIRS = UP_DOWN_DIRS
TOP_BOTTOM_DIRS = UP_DOWN_DIRS
dirs = directions
dir_rev = {
    (-1, 0): 0, 
    (0, 1): 1, 
    (1, 0): 2, 
    (0, -1): 3, 
}
compass = dirs

hex_flat_top = {
    "NW": (-.5, -1),
    "N": (-1, 0),
    "NE": (-.5, 1),
    "SE": (.5, 1),
    "S": (1, 0),
    "SW": (.5, -1),
}

hex_pointed_top = {
    "NW": (-1, -.5),
    "NE": (-1, .5),
    "E": (0, 1),
    "W": (0, -1),
    "SE": (1, .5),
    "SW": (1, -.5),
}

complement = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L",
}
complements = complement
comps = complements

adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]
adj8 = [(i, j) for i in range(-1, 2)
        for j in range(-1, 2)
        if not (i == 0 and j == 0)]
    
# ways = choose
#aliases
dirs = directions
ajd = adj
ajd4 = adj
adj4 = adj
cardinals = adj
ajd8 = adj8
all_touching = adj8

comb = combinations
combs = combinations
combos = combinations
combos_with_rep = combinations_with_replacement
combos_with_rec = combinations_with_replacement
comb_rep = combinations_with_replacement
combrep = combinations_with_replacement
perms = permutations



class AdventInput:
    '''Takes string name of file to read'''
    def __init__(self, input_file=None,data=None):
        '''has self.line(s), self.value(2), self.data'''
        if input_file is None:
            self.setup(data)
            return
        full_input_path = os.path.join(sys.path[0], input_file)
        # print(full_input_path)
        with open(full_input_path) as f:
            self.data = f.read()
        self.setup(self.data)
    def setup(self, data : str):
        self.lines : list[str] = data.splitlines()
        self.paragraphs = data.split("\n\n")
        self.paras = self.paragraphs
        self.para = self.paragraphs
        if len(self.lines) == 1:
            self.line = data
            self.word = data
        # if all(x.isnumeric() for x in self.lines) and len(self.lines) < 3:
            # self.lines = nums(data)
        self.data = data
        self.grid = to_grid(data)
        self.as_grid = to_grid(data)
        self.board = self.grid
        self.all = data
        self.values=nums(data)
        self.nums=nums(data)
        self.nums2=nums(data, False)
        self.values2=nums(data, False)
        if len(data) < 15 and data.isnumeric():
            self.value = self.val = self.data = self.num = int(data)
    def split(self, sep, max_=-1):
        return self.data.split(sep, max_)

# class Maze:
#     def __init__(self, a):
#         self.board = read_board(a)


def lmap(func, *iterables):
    '''shorter version of list(map(...))'''
    return list(map(func, *iterables))

l_map= lmap

def head(x):
    '''returns the first element of x'''
    return list(x)[0]
first = head
fst = first

def last(x):
    '''returns the last element of x'''
    return x[len(x)-1]

def tail(x):
    '''returns the second element of x onward'''
    return x[1:]

def abs_sum(x):
    '''returns the sum of the absolute values of x'''
    return sum(abs(i) for i in x)

def num_to_list(x):
    '''returns list
    35678 -> [3, 5, 6, 7, 8]'''
    return [int(y) for y in str(x)]
big_num_to_list = num_to_list
bignumlist = num_to_list
bigintlist = num_to_list
num_as_list = num_to_list
def irange(start, stop, step=1):
    '''makes an intelligent range that is inclusive'''
    return range(start, stop+1, step) if start <stop else range(start, stop-1, -1 if step == 1 else step)

rangei = irange

class ibounds:
    def __init__(self, start, stop, step=1) -> None:
        self.range = range(start, stop+1, step) if start <= stop else range(start, stop-1, -1 if step == 1 else step)
        self.start = self.range.start
        self.stop = self.range.stop
        self.step = self.range.step
    def __contains__(self, other):
        if type(other) in [range, ibounds]:
            return other.start in self.range and other.stop-other.step in self.range
        return other in self.range
    def overlaps(self, other):
        if type(other) in [range, ibounds]:
            return other.start in self.range or other.stop-other.step in self.range or\
                   self.start in other.range or self.stop-self.step in other.range
        return False
    def __repr__(self) -> str:
        return str(self.range)

Bounds = ibounds 

def bounded(number, lo, hi):
    return max(min(number, hi), lo)

def in_bounds(board: list[list], y, x) -> bool:
    '''returns True if (y, x) is in bounds of the board'''
    if isinstance(board, dict):
        return (y, x) in board
    return 0 <= y < len(board) and 0 <= x < len(board[y])


def debug(*args, **kwargs):
    # print(sys.argv)
    if ("d" in sys.argv or "debug" in sys.argv):
        print(*args, **kwargs, file=sys.stderr)

def str_int(a):
    '''gets string and integer pairs from a'''
    pat = r"(?m)^([A-Za-z]+).*?(\d+)"
    if "\n" not in a:
        word, number =  re.match(pat, a).groups()
        return word, int(number)
    return [(word, int(number)) for word, number in re.findall(pat, a)]
word_num = str_int
word_num_pair = str_int
word_num_pairs = str_int

def int_str(a):
    '''gets string and integer pairs from a'''
    if "\n" not in a:
        word, number =  re.match(r"(?m)^(\d+).*?([A-Za-z]+)", a).groups()
        return int(number), word
    return [(int(number), word) for number, word in re.findall(r"(?m)^(\d+).*?([A-Za-z]+)", a)]
    # ret = []
    # for line in a.split('\n'):
    #     left, right = line.split(delim) if delim is not None else line.split()
    #     right = int(right)
    #     ret.append((left, right))
    # return ret

# def movement(a):
#     ret = []
#     for line in a.split('\n'):
#         s, n = re.match(r"(.+?)(\d+)", line).groups()
#         n = int(n)
#         ret.append((s, n))
#     return ret

def none(_iterable):
    return not any(_iterable)

def words(a):
    '''same as split'''
    return a.split()

def neg_each(a):
    return [-1*i for i in a]

def alphawords(a):
    '''returns a list of all the alpha words in a'''
    return re.findall(r"[a-zA-Z]+", a)
alphwords=alphawords
def nums(a : str, negs=True):
    '''Returns a list with all the numbers from a string'''
    pattern = r"-?\d+" if negs else r"\d+"
    return [int(n) for n in re.findall(pattern, a.strip())]

def single_nums(a : str, negs=True):
    '''Returns a list with all the numbers from a string'''
    pattern = r"-?\d" if negs else r"\d"
    return [int(n) for n in re.findall(pattern, a.strip())]

def num(a : str, negs=True):
    '''Returns the first number found in a'''
    pattern = r"-?\d+" if negs else r"\d+"
    return int(re.search(pattern, a).group(0))

def num_ranges(a : str, negs=False):
    '''Returns a list with the numbers from a string'''
    if type(a) == str:
        a = a.strip().split('\n')
    return [
        nums(x, negs)
        for x in a]

def char_range(start : str, stop : str):
    '''returns a list of characters in a range (inclusive)'''
    return [chr(i) for i in range(ord(start), ord(stop) + 1)]
crange = char_range
c_range = char_range

def first_last(a):
    '''gets the first and last value from a'''
    return a[0], a[-1]

def apply_while(f, a, condition):
    '''continuously applies f to a (list), as long as condition is true'''
    ret = []
    while condition(a):
        a = f(a)
        if condition(a):
            ret.append(a)
    return ret

reduce_while = apply_while

def to_grid(a, as_dict=False):
    '''returns a 2d list or dict from a string'''
    temp = lmap(list, a.split('\n'))
    return to_dict(temp) if as_dict else temp

read_grid = to_grid
grid = to_grid
to_board = to_grid

def board_to_string(board: list[list[str]]):
    return "\n".join("".join(board[y]) for y in range(len(board)))

def to_dict(a, convert_numbers=True):
    '''converts 2D list to a dict of (y, x) -> value'''
    if isinstance(a, str):
        a = a.split("\n")
    return {(y, x) : (int(a[y][x]) if (convert_numbers and a[y][x].isnumeric()) else a[y][x]) for y in range(len(a)) for x in range(len(a[y]))}

list_to_dict = to_dict

def lines(a):
    '''returns list of lines in a'''
    return a.split("\n")

def read_dd_list(a : str, delim : str, right_delim=None):
    '''reads a dictionary where there are multiple values at each key'''
    ret = dd(list)
    for line in a.split('\n'):
        left, right = line.split(delim)
        if right_delim is not None:
            right = right.split(right_delim)
            ret[left].extend(right)
        else:
            ret[left].append(right)
    return ret

read_dict_list = read_dd_list

def read_dict(a, key_val_delim, entry_delim='\n'):
    '''converts string to dictionary'''
    ret = {}
    for line in re.split(rf"{entry_delim}", a):
        left, right = line.strip().split(key_val_delim)
        ret[left] = right
    return ret

make_dict = read_dict

def count_around(a, y, x, look_for=".", where_to_look=adj4):
    '''counts how many spots around y, x == look_for
    AAA
    .B.
    ...
    B has 1 A if adj4, 3 if adj8
    '''
    if type(a) == list:
        a = list_to_dict(a)
    return sum(a[y + dy, x + dx] == look_for for dy, dx in where_to_look if (y + dy, x + dx) in a)

def count_around_all(a, look_for='.', where_to_look=adj4):
    '''counts for every tile how many "look_for" are around it
    a is list[list] or dict[y, x] = character
    '''
    if isinstance(a, list):
        a = to_dict(a)
    return {point : count_around(a, *point, look_for, where_to_look) for point in a}

count_all_around = count_around_all
count_neighbors = count_around
count_all_neighbors = count_around_all
def num_list(a, sep="\n", negs=True):
    '''Returns a 2D list with only the numbers
     from each line of a string or a list'''
    # pattern = r"-?\d+" if negs else r"\d+"
    if type(a) == str:
        a = a.strip().split(sep)
    return [n for x in a if (n := nums(x, negs) ) != []]

get_num_list = num_list
read_nums = num_list
read_all_nums = num_list
def prod(x):
    '''returns the product of all elements 
    in a list multiplied together
    '''
    res = 1
    for i in x:
        res *= i
    return res

product = prod

# pow()
#aliases
num_lists = num_list
nums_lists = num_list
nums_list = num_list
nums2 = num_list
ints = nums
enu = enumerate

def tsorted(a, key=None, reverse=False):
    '''returns the tuple(sorted(a)) version of a'''
    return tuple(sorted(a, key=key, reverse=reverse))

t_sorted = tsorted

def str_sorted(a, key=None, reverse=False):
    '''returns "".join(sorted(a)) version of a'''
    return "".join(sorted(a, key=key, reverse=reverse))
strsorted = str_sorted

def rev(a):
    '''returns list(reversed(a))'''
    return list(always_reversible(a))
lrev = rev

def rev_dict(d):
    return {v:k for k, v in d.items()}
reverse_dict=rev_dict

def group_up(iterable, key):
    '''puts elements from iterable into groups
    based on key, i.e. points in a grid'''
    groups = [{z} for z in iterable]
    changed = True
    while changed:
        changed = False
        pos2 = 0
        while 0 <= pos2 < len(groups):
            pos = 0
            while 0 <= pos < len(groups):
                # print(pos2, pos)
                # print(group)
                if pos2 == pos:
                    pos += 1
                    continue
                if any(key(x, y) for x in groups[pos2] for y in groups[pos]):
                    groups[pos2] |= groups[pos]
                    groups.pop(pos)
                    changed = True
                    continue
                pos += 1

            pos2 += 1
            print(pos2)
    # for p in iterable:
    #     found = False
    #     if not found:
    #         groups.append([p])
    return groups
# def flatten(*list_list):
#     '''takes a list of lists and combines them into one list'''
#     temp =  list(chain.from_iterable(list_list))
#     if temp == list_list:
#         return flatten_all(list_list)
#     return temp

# def flatten_all(*list_list):
#     '''takes a list of lists and combines them into one list'''
#     ret = list(chain.from_iterable(list_list))
#     while type(ret[0]) == list:
#         ret = list(chain.from_iterable(ret))
#     return ret
flatten_all = collapse
flatten_complete = flatten_all

def rotate(board, times=1):
    '''rotates a 2d list by 90 degrees'''
    new = deepcopy(board)
    for _ in range(times):
        new = [[new[i][j] for i in range(len(new)-1, -1, -1)]
                for j in range(len(new[0]))]
    return new

rotate90=rotate
rot=rotate


def flip(board):
    '''flip a 2d list by 180 degrees over Y axis (left side becomes right)'''
    new = deepcopy(board)
    new = [line[::-1] for line in new]
    return new

def orientations(board):
    new = deepcopy(board)
    ret = [new]
    seen = {string(new)}
    for _ in range(2):
        for i in range(1, 5):
            cur =rotate(new, i)
            if string(cur) in seen:
                continue
            seen.add(string(cur))
            ret.append(cur)
        new = flip(new)
    return ret
    

transformations = orientations
oris = orientations
variants = orientations

# two_letters = print
puts = print
pritn = print
p = print
# def p(*args):
    # '''Faster way to type print'''
    # print(*args)

def pprint(a):
    '''Takes a 2d list and prints in a nice way'''
    if isinstance(a, dict):
        print("showing board")
        show_board(a)
        return
    
    for y in a:
        print("".join(list(map(str, y ))))
    print()

draw_board = pprint

def printe(a, remove_format=False):
    '''print each item of a list'''
    for i in list(a):
        if remove_format:
            print(*i)
        else:
            print(i)


def printd(a, sorted_=False):
    '''print keys and values from a dictionary'''
    to_iterate = sorted(a.items()) if sorted_ else a.items()
    for k, v in to_iterate:
        print(k, ":", v)

def get_hash(s):
    '''gets the md5 hash of a string'''
    return hashlib.md5((s).encode('utf-8')).hexdigest()

def manhat(p1, p2):
    '''returns manhattan distance between two points'''
    return sum(abs(a-b) for a, b in zip(p1, p2))
    # return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def abseach(t):
    '''returns a new list with the absolute value of each element '''
    return [abs(i) for i in t]

def show_board(board, actual_symbol=True, filler='.', lo_y=None, lo_x=None, max_y=None, max_x=None, conversions=None, ending='', func=lambda x: x, reversed_=False, show_anyway=False):
    '''Prints a defaultdict that uses (y, x) values for keys
    
    True  means # (wall) 
    False means . (open) 

    (isWall)
    '''

    if "AoC" in os.getcwd() and ("d" not in sys.argv and not show_anyway):
        return
    if type(board) == list:
        pprint(board)
        return
    if conversions is None:
        conversions = {True: "#", False: '.', "#":"#", ".":"."}
    y_dim = max(board, key=lambda x : x[0])[0] + 1 if max_y is None else max_y
    x_dim = max(board, key=lambda x : x[1])[1] + 1 if max_x is None else max_x

    lowest_x = min(j[1] for j in board) if lo_x is None else lo_x
    lowest_y = min(j[0] for j in board) if lo_y is None else lo_y
    print("x goes from", lowest_x, x_dim)
    # print(f"conversions: {conversions}")
    y_range =reversed(range(lowest_y, y_dim)) if reversed_ else  range(lowest_y, y_dim)
    print("\t", end='')
    for x in range(lowest_x, x_dim):
        print(abs(x) // 10, end='')
    print()
    print("\t", end='')
    for x in range(lowest_x, x_dim):
        print(abs(x) % 10, end='')
    print()
    for y in y_range:
        print(y, end='\t')
        for x in range(lowest_x, x_dim):
            if actual_symbol:
                print(func(board[(y, x)]) if (y, x) in board else filler, end=ending)
                continue
            if conversions:
                if board[(y, x)] in conversions:
                    print(conversions[board[(y, x)]] if (y, x) in board else filler, end=ending)
                else:
                    print(board[(y, x)] if (y, x) in board else filler, end=ending)

            elif board[(y, x)]:
                print("#", end=ending)
            else:
                print(".", end=ending)
        print()

print_board = pprint

def read_board(a, start_regex=r"S", goal_regex=r"@", wall_regex=r"#", syms=False):
    '''returns board : dictionary of (y, x) -> (bool isWall)
    start_y : (y)
    start_x : (x)
    goals : dict (y, x) -> marker
    '''
    board = dd(lambda : wall_regex)
    goals = {}
    if type(a) == str:
        a = a.strip().splitlines()
    for y in range(len(a)):
        for x in range(len(a[y])):
            if re.match(start_regex, a[y][x]):
                start_x = x
                start_y = y
            if re.match(goal_regex, a[y][x]):
                goals[(y, x)] = a[y][x]
            if syms:
                board[(y, x)] = a[y][x]
                continue
            board[(y, x)] = bool(re.match(wall_regex, a[y][x]))
    if len(goals) == 1:
        goals, = goals
    return board, start_y, start_x, *goals

def get_maze_connections(a : str, wall=r"#", touching=adj4):
    '''given maze a, returns a dict[(y, x)] : List[open_adj_spots]'''
    board = dd(set)
    if type(a) == str:
        a = a.strip().splitlines()
    # print(a)
    for y in range(len(a)):
        for x in range(len(a[y])):
            if re.fullmatch(wall, a[y][x]):
                continue
            for dy, dx in touching:
                if y+dy in range(len(a)) and x + dx in range(len(a[y])) and \
                    not re.fullmatch(wall, a[y+dy][x+dx]):
                    board[y, x].add((y+dy, x+dx))
    return board

def find_in_grid(a, look_for_regex):
    '''returns the (y, x) position of the single character to look for in a'''
    if type(a) == str:
        a = a.split("\n")
    ret = [(y, x) for y in range(len(a)) for x in range(len(a[y])) if re.fullmatch(look_for_regex, a[y][x])]
    if len(ret) == 1:
        return ret[0]
    return ret

def longest_path(inp, start, goal, wall="#"):
    '''
    start : (y, x)
    goal : (y, x)
    '''
    connections = get_adj_connections(inp, wall)
    fringe = deque([(start, 0, {start})])
    highest = -1
    while fringe:
        cur, steps, seen = fringe.pop()
        if cur == goal:
            highest = max(highest, steps)
        for spot in connections[cur]:
            if spot not in seen:
                fringe.append((spot, steps + 1, seen | {spot}))
    return highest
get_adj_connections = get_maze_connections


def get_vals_around(y, x, d, around=adj4):
    '''returns the values of the neighbors surrounding a point'''
    if isinstance(d, dict):
        return [d[y+dy, x+dx] for dy, dx in around if (y+dy, x+dx) in d]
    else:
        return [d[y+dy][x+dx] for dy, dx in around if y+dy in range(len(d)) and x+dx in range(len(d[0])) in d]

def get_around(y, x, d, around=adj4):
    '''returns the point coordinates of those around (y, x)
    i.e. around (2,2) -> [(1,2),(3,2),(2,3),(2,1)]
    '''
    return [(y+dy, x+dx) for dy, dx in around if (y+dy, x+dx) in d]
get_neighbors = get_vals_around

def dijkstra(board : dict, startY, startX, goalY, goalX):
    '''
    given a board : dict[y, x] -> cost and starting and
    ending y and x, computes the minimum cost to get from
    start to goal'''
    goal = (goalY, goalX)
    # print(goal)
    fringe = ([(0, (startY, startX))])
    heapq.heapify(fringe)
    seen = dd(lambda : inf)
    while fringe:
        steps, (y, x) = heapq.heappop(fringe)
        if seen[y, x] <= steps:
            continue
        seen[y, x] = min(seen[y, x], steps)
        if (y, x) == goal:
            # print("stopped")
            return (steps)
        for dy, dx in adj:
            n = (dy+y, dx +x)
            if n in board:
                heapq.heappush(fringe, (board[n] + steps, n))
dikestra = dijkstra

def bfs(start_y, start_x, goalY, goalX, board, max_steps=float("+inf"), wall=True, just_steps=True, longest=False):
    '''Returns steps from start to goal, and optionally seen (dict of (posY, posX) : steps away)
    
    given starting x and y, and goalX and goalY, and 
    dictionary of (y, x) as keys and bool values (True for # wall,
    False for . open)'''
    fringe = deque([(start_y, start_x, 0)])
    seen = dd(lambda: float("+inf"))
    seen[(start_y, start_x)] = 0
    yDim = max(j[0] for j in board.keys()) + 1
    xDim = max(j[1] for j in board.keys()) + 1
    def add_spot(newY, newX, steps):
        pot = (newY, newX)
        if (0 <= newY < yDim and 0 <= newX < xDim and board[pot] != wall) and steps + 1 < seen[pot]:
            fringe.append((newY, newX, steps + 1))
            seen[pot] = steps + 1
    while fringe:
        y, x, steps = fringe.popleft()
        if not longest and steps >= max_steps:
            continue
        if (y, x) == (goalY, goalX):
            if just_steps:
                return steps
            return steps, seen
        for dy, dx in adj4:
            add_spot(y + dy, x + dx, steps)
    if just_steps:
        return steps
    return steps, seen

def solve_maze(a, start_regex=r"S", goal_regex=r"@", wall_regex=r"#", syms=False, max_steps=float("+inf")):
    '''returns a list of distances to goals, or just cost if 1 goal'''
    board, start_y, start_x, goals = read_board(a.strip(), start_regex, goal_regex, wall_regex, syms=False)
    costs = [
        bfs(
            start_y,
            start_x,
            end_y,
            end_x,
            board,
            max_steps,
            True if not syms else wall_regex
        )
        for end_y, end_x in goals.keys()
    ]
    if len(costs) == 1:
        return costs[0]
    return costs
        # print(steps)
        # print(seen)

def path_sum(path, cost_dict):
    '''returns the cost of 1 path (iterable) based on cost_dict[(a, b)] = cost'''
    return sum(cost_dict[path[i], path[i+1]] for i in range(len(path) - 1))

    
path_cost = path_sum
cheapest_stops = path_sum
def all_path_sums(must_include, cost_dict, start=None, path_size=None):
    '''given a cost dict with x1, x2 = cost '''
    return [path_sum(([start] if start is not None else []) + list(perm), cost_dict) for perm in permutations(must_include, path_size if path_size is not None else len(must_include))]
all_path_costs = all_path_sums
def find_all_path_costs(inp, start_regex, end_regex):
    '''returns a dict with path costs from d1 -> d2'''
    cache = {}
    dests =[start_regex] + list(set(re.findall(end_regex, inp)))
    print("dests", dests)
    for start, end in combs(dests, 2):
        cache[start, end] = solve_maze(inp, start_regex=start, goal_regex=end)
        cache[end, start] = cache[start, end] 
    return cache

# def board_str(board, sep=''):
#     '''return the 1D version of a 2D list'''
#     return reduce(lambda x, y: x + y, map())
# def lcm(a, b):
#     '''returns the least common multiple of a and b'''
#     return abs(a*b) // gcd(a, b)

def string(lis : list, sep=''):
    '''given a list, a string is returned with sep as separator'''
    if isinstance(lis, int):
        return list(str(lis))
    lis = list(lis)
    if type(lis[0]) == list:
        lis = reduce(lambda x, y: x + y, lis)
    return sep.join(list(map(str, lis)))
str_list = string
list_to_big_num =string
def mult_dict_values(d, multiplier):
    '''multiplies all values in dictionary by multiplier'''
    return {x: d[x] * multiplier for x in d}

def least_common(a: str):
    counts = Counter()
    for letter in a.strip():
        counts[letter] += 1
    return min(counts.keys(), key=lambda x: counts[x])
    


def elementwise(a, b, operation=op.add):
    '''
    a = [1, 2, 3]
    b = [10, 20, 30]
    operation = op.add
    = [11, 22, 33]
    '''
    return [operation(x, y) for x, y in zip(a, b)]

def elementwise_tup(a, b, operation=op.add):
    return tuple(element_wise(a, b, operation))

element_wise = elementwise
element_wise_tup = elementwise_tup

streaks = run_length.encode
parts = chunked

split_into_n_groups=more_itertools.distribute
split_up=chunked
make_groups_size_n = chunked
get_groups_size_n = chunked
groups = chunked
def first_repeat(a):
    '''returns the first element to be seen twice in a'''
    seen = set()
    for i in a:
        if i in seen:
            return i
        seen.add(i)

def dict_to_list(d):
    '''converts a dict[(y, x)] to a 2D list'''
    # ret = [[]]
    min_y = min(d.keys(), key=lambda x: x[0])[0]
    max_y = max(d.keys(), key=lambda x: x[0])[0]
    min_x = min(d.keys(), key=lambda x: x[1])[1]
    max_x = max(d.keys(), key=lambda x: x[1])[1]
    # for y in range(min_y, max_y+1):
        # for x in range(min_x, max_x+1):
            # ret[-1].append(d[y, x])
        # ret.append([])
    return [[d[y, x] for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]

    # for y, x in d:
        # ret.append(d[])
def transpose(board):
    '''trasposes a 2D list'''
    if isinstance(board, str):
        board = board.split("\n")
    return [[board[y][j] for y in range(len(board))] for j in range(len(board[0]))]
def get_subsection(board, start_y, start_x, size_y=3, size_x=3):
    '''gets a region from a 2D list board =

            [['t', 'h', 'e'], 
             ['c', 'a', 't'], 

             ['d', 'o', 'g']]

    get_region(board, 1, 1, 2, 2)
    = ['a', 't', 'o', 'g']
    '''
    return [
        board[start_y + y][start_x + x]
        for y in range(size_y)
        for x in range(size_x)
    ]

get_region = get_subsection
get_section = get_subsection

# get_subsection()
def ans(x, should_exit=False, sep=""):
    '''copies an answer to the clipboard'''
    answer = sep.join(lmap(str,x)) if type(x) == list else str(x)
    if type(x) == list and len(x) == 1:
        answer = x[0]
    # print("about to copy to clipboard:")
    print("real:", answer)

    if using_pypy:
        # print("COPY THIS TO THE CLIPBOARD!!!!")
        os.system(f"echo {answer} | clip.exe")
    else:
        pyperclip.copy(answer)
    print("copied")
    if should_exit:
        exit()

ans2=partial(ans, should_exit=True)

def die():
    print("=======died as requested========")
    print("================================")
    exit()

def validate(value, expected):
    if DEBUG:
        print(value)
        print("expected")
        print(expected)
    assert expected == value

