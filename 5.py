from AoCLibrary import *
with open("input5.txt") as f:
    real_input = f.read()

from attrs import define, field
@define
class Conversion:
    source_start: int
    dest_starts_x_higher: int
    source_exclusive_upper: int

    def get_range(self):
        return range(self.source_start, self.source_exclusive_upper)

    def convert_value(self, to_convert: int):
        offset = to_convert - self.source_start
        return self.source_start + self.dest_starts_x_higher + offset


def main(a : str):
    def seed_to_location(seed: int):
        current_value = seed
        for from_type in order:
            for bound in all_conversions[from_type]:
                if current_value in bound.get_range():
                    current_value = bound.convert_value(current_value)
                    break
            #no logic needed for mapping to itself
        return current_value
    
    a = a.strip()
    inp = AdventInput(data=a)
    
    seeds = nums(inp.para[0])
    all_conversions: dict[str, list[Conversion]] = dd(list)
    order = []

    x_to_y = {}
    
    for section in inp.para[1:]:
        key = None
        for line in lines(section):
            cur_line_nums = nums(line)
            if cur_line_nums:
                dest_start, source_start, range_len = cur_line_nums
                all_conversions[key].append(Conversion(source_start, dest_start - source_start, source_start + range_len))
            else:
                key, _, to = line.split()[0].split("-")
                x_to_y[key] = to
                order.append(key)
                continue
    order.append(to)

    def get_min_location1():
        return min(seed_to_location(seed) for seed in seeds)
    
    def part2():
        lo = inf
        groups = list(get_groups_size_n(seeds, 2))
        print("total groups", len(groups))
        for i, (start, range_len) in enu(groups):
            print("starting group", i, start, range_len)
            for i in range(start, start + range_len):
                if i % 10_000_000 == 0:
                    print(i)
                lo = min(lo, seed_to_location(i))
        return lo
    
    print(get_min_location1())
    return part2()


samp = r"""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

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