from AoCLibrary import *
with open("input18.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    return solve(inp.lines, part2=False), solve(inp.lines, part2=True)

def solve(lines: list[str], part2=False):
    pos_y = 0
    pos_x = 0
    x_coords = [pos_x]
    y_coords = [pos_y]
    perimeter_len = 0
    for line in lines:
        dir_, amount, color = line.split()
        if part2:
            dy_dx, amount = get_part2_dir_and_amount(color)
        else:
            dy_dx = dirs[dir_]
        amount = int(amount) 
        dy, dx = dy_dx
        pos_x += dx * amount
        pos_y += dy * amount
        x_coords.append(pos_x)
        y_coords.append(pos_y)
        perimeter_len += amount

    area = polygonArea(x_coords, y_coords)
    answer = area + perimeter_len / 2 + 1
    assert answer == int(answer)
    return int(answer)

def get_part2_dir_and_amount(color):
    # 0 means R, 1 means D, 2 means L, and 3 means U
    num_to_dir = {
        3: (-1, 0),
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
    }
    move_amount = int(color[2:-2], 16)
    new_dir = num_to_dir[int(color[-2])]
    return new_dir, move_amount


def polygonArea(x_coord_list, y_coord_list):
    area = 0.0
    for i in range(0,len(x_coord_list)):
        next_pos = (i + 1) % len(x_coord_list)
        area += (x_coord_list[i] * y_coord_list[next_pos]) - (
            x_coord_list[next_pos] * y_coord_list[i]
        )
    return int(abs(area / 2.0))

def bfs2(start_y, start_x, board, wall=True):
    fringe = deque([(start_y, start_x)])
    while fringe:
        y, x = fringe.popleft()
        if board[y, x] == wall:
            continue
        board[y, x] = wall
        for dy, dx in adj4:
            fringe.append((y + dy, x + dx))
    return board



samp = r"""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)

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