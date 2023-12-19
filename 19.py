from AoCLibrary import *
import attrs
with open("input19.txt") as f:
    real_input = f.read()

@attrs.define
class PartBound:
    start: int
    stop: int
    # def __init__(self, start, stop) -> None:
    #     self.start = start
    #     self.stop = stop

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    rules, parts = inp.para
    rules = format_rules(rules)

    part1 = sum(sum(x.values()) for x in get_accepted_outputs(rules, parts)) 
    part2 = get_all_possible(rules)
    return part1, part2 

def get_accepted_outputs(rules, parts):
    outputs = dd(list)
    parts = re.sub(r'([xmas])', r'"\1"', parts).replace("=", ':').splitlines()
    parts = lmap(eval, parts)
    for part in parts:
        outputs[find_rule_for_part(rules, part)].append(part)
    return outputs['A']


def format_rules(rules):
    rules = rules.splitlines()
    rules_dict = {}
    for rule in rules:
        name = re.search(r'^\w+', rule).group()
        conditions = re.search(r'\{(.+)\}', rule).group(1)
        conditions = conditions.split(',')
        rules_dict[name] = conditions
    return rules_dict

def find_rule_for_part(rules: dict[str, list], part: dict):
    current_rule = "in"
    while current_rule not in ['R', 'A']:
        for condition in rules[current_rule]:
            # on the A or R or last condition case
            if ":" not in condition:
                current_rule = condition
                break
            left, result = condition.split(":")
            left = f"{part}['{left[0]}']{left[1:]}"
            eval_result = eval(left)
            if eval_result:
                current_rule = result
                break
    return current_rule
            
def get_all_possible(rules: dict[str, list]):
    starting_bounds = {
        "x": PartBound(1, 4001), 
        "m": PartBound(1, 4001), 
        "a": PartBound(1, 4001), 
        "s": PartBound(1, 4001)
    }
    fringe = deque([("in", deepcopy(starting_bounds))])
    
    ret = []
    while fringe:
        cur, bounds = fringe.pop()
        if cur in ['A', 'R']:
            if cur == 'A':
                ret.append(deepcopy(bounds))
            continue
        current = deepcopy(bounds)
        for condition in rules[cur]:
            if ":" not in condition:
                fringe.append((condition, current))
                break
            xmas_letter = condition[0]
            temp = deepcopy(current)
            to_go_to = condition.split(":")[-1]
            if "<" in condition:
                temp[xmas_letter].stop = min(num(condition), temp[xmas_letter].stop)
                fringe.append((to_go_to, deepcopy(temp)))
                current[xmas_letter].start = max(num(condition), current[xmas_letter].start)
            else:
                # a > 3000
                temp[xmas_letter].start = max(temp[xmas_letter].start, num(condition) + 1)
                fringe.append((to_go_to, deepcopy(temp)))
                current[xmas_letter].stop = min(num(condition) + 1, current[xmas_letter].stop)

    return sum(
                prod(bound_.stop - bound_.start for bound_ in bound_set.values()) 
                for bound_set in ret
            )



samp = r"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""".lstrip("\n")


# samp = r"""
# in{a>3333:foo,A}
# foo{m>838:don,A}
# don{m<2838:A,s>1770:A,m>3801:A,A}

# {x=787,m=2655,a=1222,s=2876}

# """.lstrip("\n")

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