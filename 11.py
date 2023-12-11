from AoCLibrary import *
with open("input11.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    board = a.splitlines()
    empty_y_coords = get_empty_line_numbers(board)
    board = transpose(board)
    empty_x_coords = get_empty_line_numbers(board)
    board = transpose(board)
    y_dim = len(board)
    x_dim = len(board[0])
    board = to_dict(board)
    galaxies = []
    for y in range(y_dim):
        for x in range(x_dim):
            if board[y, x] == '#':
                galaxies.append((y, x))
                
    distances = get_distances(galaxies, empty_y_coords, empty_x_coords, 2)
    distances2 = get_distances(galaxies, empty_y_coords, empty_x_coords, 1000000)
    return sum(distances), sum(distances2)

def get_distances(galaxies, empty_y_coords, 
                empty_x_coords, expand_mult):
    distances = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            y_lo = bisect.bisect_left(empty_y_coords, galaxies[i][0])
            y_hi = bisect.bisect_right(empty_y_coords, galaxies[j][0])
            
            x_lo = bisect.bisect_left(empty_x_coords, galaxies[i][1])
            x_hi = bisect.bisect_right(empty_x_coords, galaxies[j][1])
            coord_diff = manhat(galaxies[i], galaxies[j])
            y_extra = abs(y_hi - y_lo)
            x_extra = abs(x_hi - x_lo )
            for change in [y_extra, x_extra]:
                coord_diff += change * (expand_mult-1)
            distances.append(coord_diff)
    return distances

            
def is_empty_line(board, y):
    return ''.join(board[y]).replace(".", "") == ''

def get_empty_line_numbers(board):
    return [y for y in range(len(board)) if is_empty_line(board, y)]
    
    

samp = r"""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....


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