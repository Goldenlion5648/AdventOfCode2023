from AoCLibrary import *
with open("input9.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    part1 = sum(solve_for_line(nums(line)) for line in inp.lines)
    part2 = sum(solve_for_line(nums(line)[::-1]) for line in inp.lines)
    return part1, part2

def solve_for_line(line):
    seen = [line]
    difs = get_difs(line)
    seen.append(difs)
    while True:
        difs = get_difs(difs)
        seen.append(difs)
        if all(x == 0 for x in difs):
            break
    
    for i in range(len(seen)-2, -1, -1):
        seen[i].append(seen[i+1][-1] + seen[i][-1])
    return seen[0][-1]
    
def get_difs(current_line):
    difs = [
        current_line[i+1] - current_line[i] 
        for i in range(len(current_line)-1)
    ]
    return difs
        
        
    



samp = r"""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45

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