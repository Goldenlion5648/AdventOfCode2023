from AoCLibrary import *
with open("input2.txt") as f:
    real_input = f.read()

def main(a : str, part2=False):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    for line in inp.lines:
        bad = False
        idx = nums(line)[0]
        hi_red = 0
        hi_blue = 0
        hi_green = 0
        for game in line[line.index(":") + 1:].split("; "):
            red = int((re.findall(r"(\d+) red", game) or ["0"])[0])
            green = int((re.findall(r"(\d+) green", game) or ["0"])[0])
            blue = int((re.findall(r"(\d+) blue", game) or ["0"])[0])
            hi_red = max(red, hi_red)
            hi_blue = max(blue, hi_blue)
            hi_green = max(green, hi_green)
            bad = bad or red > 12 or green > 13 or blue > 14
        if part2:
            ret += hi_blue * hi_green * hi_red
        else:
            if not bad:
                ret += idx
    return ret

samp = r"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

""".lstrip("\n")

sample_answer = main(samp)
print("sample", sample_answer)
sample_answer = main(samp, True)
print("sample", sample_answer)

ans(main(real_input))
ans(main(real_input,True))