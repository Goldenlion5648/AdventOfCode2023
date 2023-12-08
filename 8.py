from AoCLibrary import *
with open("input8.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    G = {}
    instructions = inp.lines[0]
    for line in inp.lines[2:]:
        start, left, right = re.findall(r'\w+', line)
        G[start] = (left, right)

    return search(G, instructions), search2(G, instructions, [node for node in G if node.endswith('A')])
    

def search(G, instructions):
    fringe = deque([('AAA', 0, 0)])
    while fringe:
        node, instruct_pos, steps = fringe.popleft()
        if node == 'ZZZ':
            return steps
        if instructions[instruct_pos%len(instructions)] == 'L':
            fringe.append((G[node][0], instruct_pos + 1, steps + 1))
        else:
            fringe.append((G[node][1], instruct_pos + 1, steps + 1))
    assert False

def search2(G, instructions, all_starting_positions:list[str]):
    fringe = deque()
    for start in all_starting_positions:
        fringe.append((start, 0, 0))
    spot_to_steps = {}
    while fringe:
        node, instruct_pos, steps = fringe.popleft()
        if node.endswith("Z"):
            spot_to_steps[node] = steps
            continue
        if instructions[instruct_pos%len(instructions)] == 'L':
            fringe.append((G[node][0], instruct_pos + 1, steps + 1))
        else:
            fringe.append((G[node][1], instruct_pos + 1, steps + 1))
    return lcm(*spot_to_steps.values())



if "s" in sys.argv:
    exit()
result = main(real_input)
if result is not None:
    ans(result)