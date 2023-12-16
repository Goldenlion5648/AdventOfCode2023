from AoCLibrary import *
with open("input16.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    board = to_board(a, True)
    board_list = to_board(a)
    y_dim = len(board_list)
    x_dim = len(board_list[0])


    best = 0
    for y in range(y_dim):
        best = max(best, travel(board, y, 0, Directions.EAST))
        best = max(best, travel(board, y, x_dim -1, Directions.WEST))
    for x in range(x_dim):
        best = max(best, travel(board, 0, x, Directions.SOUTH))
        best = max(best, travel(board, y_dim -1, x, Directions.NORTH))
    return best
        

def travel(board, start_y, start_x, start_dir):
    fringe = deque([((start_y, start_x), start_dir)])
    seen = {}
    while fringe:
        cur_pos, dir_traveling = fringe.popleft()
        # show_board(board)
        # if board[cur_pos]
        if cur_pos not in board:
            continue
        state = cur_pos, dir_traveling
        if state in seen:
            continue
        seen[state] = True
        if board[cur_pos] == '|':
            if dir_traveling in SIDE_DIRS:
                for bounce_dir in UP_DOWN_DIRS:
                    fringe.append(get_next_pos(bounce_dir, cur_pos))
            else:
                fringe.append(get_next_pos(dir_traveling, cur_pos))
        elif board[cur_pos] == '-':
            if dir_traveling in UP_DOWN_DIRS:
                for bounce_dir in SIDE_DIRS:
                    fringe.append(get_next_pos(bounce_dir, cur_pos))
            else:
                fringe.append(get_next_pos(dir_traveling, cur_pos))
        elif board[cur_pos] == '/':
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.EAST, Directions.NORTH, cur_pos))
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.NORTH, Directions.EAST, cur_pos))
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.WEST, Directions.SOUTH, cur_pos))
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.SOUTH, Directions.WEST, cur_pos))
        elif board[cur_pos] == '\\':
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.SOUTH, Directions.EAST, cur_pos))
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.EAST, Directions.SOUTH, cur_pos))
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.WEST, Directions.NORTH, cur_pos))
            fringe.extend(get_angle_bounce_result(dir_traveling, Directions.NORTH, Directions.WEST, cur_pos))
        elif board[cur_pos] in ['.', '#']:
            # board[cur_pos] = '#'
            fringe.append(get_next_pos(dir_traveling, cur_pos))
        # else:
            # assert False, board[cur_pos]
    just_positions = get_just_positions(seen)
    # show_board({pos: '#' for pos in just_positions})
    # print(just_positions)
    return len(just_positions)


def get_just_positions(seen):
    return {x for x, y in seen}


def get_next_pos(dir_traveling: Directions, cur_pos):
    return (element_wise_tup(dir_traveling.value, cur_pos), dir_traveling)

def get_angle_bounce_result(dir_traveling, incoming_dir, out_direction, cur_pos):
    if dir_traveling == incoming_dir:
        return [(element_wise_tup(out_direction.value, cur_pos), out_direction)]
    return []




samp = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....

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