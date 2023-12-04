from AoCLibrary import *
with open("input4.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    G = dd(list)
    for i in range(len(inp.lines)):
        G[i+1].append(1)
    for n, line in enu(inp.lines, 1):
        line = line.split(":")[1]
        winning, other = line.split("|")
        winning = nums(winning)
        other = nums(other)
        matching = len(set(winning) & set(other)) 
        if matching:
            cur = 2 ** (matching- 1)
            ret += cur
            for x in range(matching):
                G[n+x+1].extend([1] * len(G[n]))
            
    return (ret, sum(len(x) for x in G.values()))




samp = r"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

""".lstrip("\n")

if samp and "r" not in sys.argv:
    sample_answer = main(samp)
    print("sample", sample_answer)

ans(main(real_input))