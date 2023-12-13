from AoCLibrary import *
with open("input12.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    
    return solve_for_input(inp.lines), solve_for_input(inp.lines, 5)

def solve_for_input(lines, mult=1):
    ret = 0
    for line in lines:
        counts = nums(line)
        spring = line.split()[0]
        ways_for_line = get_count('?'.join([spring]*mult), tuple(counts)*mult)
        ret += ways_for_line
    return ret

@cache
def get_count(line: str, counts: tuple[int]):
    debug(line, counts)
    if len(counts) == 0:
        debug("stopped 1")
        if "#" in line:
            return 0
        debug("was valid" + '='*30)
        return 1
    ret = 0
    for i in range(len(line)):
        if line[i] == '.':
            continue
        debug(i, "original line was", line, counts)
        pat = r'^(\?|\#){' + str(counts[0]) + r'}(\.|\?|$)'
        if re.search(pat, line[i:]):
            ret += get_count(line[i+counts[0]+1:], counts[1:])
        if line[i] == '#':
            break
    
    return ret


samp = r"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
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