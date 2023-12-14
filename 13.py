from AoCLibrary import *
with open("input13.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    part1_ret = 0
    part2_ret = 0

    for pattern in inp.para:
        pattern = to_board(pattern)
        original_top_bottom = get_top_to_bottom_fold_value(pattern)
        original_left_right = get_left_to_right_fold_value(pattern)
        part1_ret += original_left_right + (original_top_bottom * 100)
        found = False
        for swapped in get_single_flipped_pattern(pattern):
            current_value = get_top_to_bottom_fold_value(swapped, original_top_bottom) * 100
            if current_value != 0:
                part2_ret += current_value
                found = True
                break
            
            current_value = get_left_to_right_fold_value(swapped, original_left_right)
            if current_value != 0:
                part2_ret += current_value
                found = True
                break
        assert found
    return part1_ret, part2_ret

def get_single_flipped_pattern(pattern):
    opposite = {
        ".":"#",
        "#":"."
    }
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            current = deepcopy(pattern)
            current[y][x] = opposite[current[y][x]]
            yield current
    
    
def get_left_to_right_fold_value(pattern, val_to_ignore=-1):
    return get_top_to_bottom_fold_value(transpose(deepcopy(pattern)), val_to_ignore)
    
    
def get_top_to_bottom_fold_value(pattern, val_to_ignore=-10):
    for y in range(len(pattern)-1):
        good = True
        offset = 0
        for y2 in range(y+1, len(pattern)):
            top = y - offset
            bottom = y2
            if top < 0 or bottom >= len(pattern):
                break
            if pattern[top] != pattern[bottom]:
                good = False
                break
            offset += 1
        if good and y + 1 != val_to_ignore:
            return y + 1
    return 0





samp = r"""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

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