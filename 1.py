from AoCLibrary import *
with open("input1.txt") as f:
    real_input = f.read()

def part1(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    
    for line in inp.lines:
        n = []
        for letter in line:
            if letter.isdigit():
                n.append(int(letter))

        a, b = n[0], n[-1]
        ret += a * 10 + b
    return ret
    
def part2(a: str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0

    convert = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine": 9
    }
    for line in inp.lines:
        n = []
        cur = list(line)
        for i in range(len(line)):
            if line[i].isdigit():
                n.append(int(line[i]))
                continue

            for x in convert:
                if list(x) == cur[i:i+len(x)]:
                    n.append(convert[x])

        a, b = n[0], n[-1]
        ret += a * 10 + b
    return ret



ans(part1(real_input), should_exit=False)
ans(part2(real_input))