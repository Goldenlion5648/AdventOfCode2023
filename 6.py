from AoCLibrary import *
with open("input6.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 1
    times = nums(inp.lines[0])
    dists = nums(inp.lines[1])
    ways = []

    for time, dist in zip(times, dists):
        ways.append(get_ways_for_race(time, dist))
    # print(ways)

    times = int(string(times))
    dists = int(string(dists))

    return prod(ways), get_ways_for_race(times, dists)

def get_ways_for_race(time, dist):
    winning_ways_for_race = 0
    for i in range(time + 1):
        cur = (time - i) * i
        if cur > dist:
            winning_ways_for_race += 1
    return winning_ways_for_race
    



samp = r"""

Time:      7  15   30
Distance:  9  40  200
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