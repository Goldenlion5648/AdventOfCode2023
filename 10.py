from AoCLibrary import *
with open("input10.txt") as f:
    real_input = f.read()

connections = {
    "|": (Directions.NORTH, Directions.SOUTH),
    "-": (Directions.EAST, Directions.WEST),
    "L": (Directions.NORTH, Directions.EAST),
    "J": (Directions.NORTH, Directions.WEST),
    "7": (Directions.SOUTH, Directions.WEST),
    "F": (Directions.SOUTH, Directions.EAST),
    ".": (),
    # "S":(Directions.NORTH, Directions.WEST)
    "S":(Directions.SOUTH, Directions.EAST)
}

def get_start_connections(board, s_y, s_x):
    ret = []
    for offset in Directions:
        cur_coords = elementwise_tup((s_y, s_x), offset.value)
        if cur_coords not in board:
            continue
        next_to = connections[board[cur_coords]]
        if Directions.opposite(offset) in next_to:
            ret.append(offset)
    return tuple(ret)



def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    board = to_dict(a, False)
    board_array = to_board(a)
    s_y, s_x = find_in_grid(a, "S")
    connections["S"] = get_start_connections(board, s_y, s_x)
    #part 1
    fringe = deque([((s_y, s_x), 0)])
    seen = {}
    while fringe:
        cur, steps = fringe.popleft()
        if cur in seen:
            continue
        seen[cur] = steps
        for change in connections[board[cur]]:
            new = tuple(element_wise(cur, change.value))
            if not in_bounds(board_array, *new):
                continue
            fringe.append((new, steps + 1))
    part1 = max(seen.values())

    # part 2
    vertical_switch_above_below = {
        "F": (0, 1),
        "L": (1, 0),
        "|": (1, 1),
        "7": (0, 1),
        "J": (1, 0),
        "S": (Directions.NORTH in connections["S"], Directions.SOUTH in connections["S"]),
    }
    return part1, get_enclosed_area(deepcopy(board), 
                                len(board_array), len(board_array[0]), seen, vertical_switch_above_below)


def get_enclosed_area(board, y_dim, x_dim, border_tiles, vertical_switch_above_below):
    enclosed = 0
    for y in range(y_dim):
        above_open = False
        below_open = False
        for x in range(x_dim):
            cur = (y, x)
            if cur in border_tiles:
                if board[cur] == '-':
                    continue
                if board[cur] in vertical_switch_above_below:
                    above_change, below_change = vertical_switch_above_below[board[cur]]
                    above_open ^= above_change
                    below_open ^= below_change
                continue

            is_inside = above_open != 0 or below_open != 0
            if is_inside:
                enclosed += 1
                board[cur] = "$"
            else:
                board[cur] = "O"
    return enclosed

    





samp = r"""
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...

""".lstrip("\n")

# samp = """
# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
# """.lstrip("\n")

# samp = """
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# """.lstrip("\n")


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