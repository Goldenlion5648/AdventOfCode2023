from AoCLibrary import *
with open("input17.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    board = to_dict(a, True)
    # print(board)
    # print("goal", goal_coords)
    # print("adj4_opposite", adj4_opposite)
    return search(board, True)

def search(board, part2=True):
    fringe = []
    heapq.heapify(fringe)
    max_repeat_allowed = 10 if part2 else 3
    heapq.heappush(fringe, (0, (0,0), [None]*max_repeat_allowed))
    seen = dd(lambda: inf)
    goal_coords = max(board.keys())
    best = inf
    highest_cost_seen = 0
    while fringe:
        cost,cur_pos, prev_steps = heapq.heappop(fringe)
        state = (cur_pos, tuple(prev_steps[-max_repeat_allowed:]))
        # debug(cost,cur_pos, prev3)
        if cur_pos not in board:
            continue
        if cost > highest_cost_seen:
            highest_cost_seen = cost
            if highest_cost_seen % 20 == 0:
                print(highest_cost_seen, len(fringe))
        if cost >= best:
            continue
        if cur_pos == goal_coords:
            if part2 and not prev_4_steps_match(prev_steps):
                continue
            best = min(best, cost)
            print(prev_steps, cost)
            continue
        if seen[state] <= cost:
            continue
        seen[state] = cost
        for dir_ in adj4:
            new = element_wise_tup(cur_pos, dir_)
            if new in board and not all(
                old_way == dir_ for old_way in prev_steps[-max_repeat_allowed:]
            ) and (prev_steps[-1] is None or prev_steps[-1] != adj4_opposite[dir_]):
                if part2:
                    if not prev_4_steps_match(prev_steps):
                        if dir_ == prev_steps[-1]:
                            heapq.heappush(fringe, (cost + board[new], new, prev_steps + [dir_]))
                    else:
                        heapq.heappush(fringe, (cost + board[new], new, prev_steps + [dir_]))
                else:
                    heapq.heappush(fringe, (cost + board[new], new, prev_steps[-max_repeat_allowed:] + [dir_]))
    # show_board({pos: "#" for pos in seen})
    return best

# def get_cost():

def prev_4_steps_match(prev_steps):
    return all(old_step == prev_steps[-1] for old_step in prev_steps[-4:])



samp = r"""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533

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