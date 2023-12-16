from AoCLibrary import *
with open("input15.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    part1 = 0
    
    boxes = dd(dict)
    for step in a.split(","):
        if "-" in step:
            label = step.strip("-")
            target_box_num = get_hash(label)
            if label in boxes[target_box_num]:
                boxes[target_box_num].pop(label)
        else:
            label, val = step.split("=")
            target_box_num = get_hash(label)
            val = int(val)
            boxes[target_box_num][label] = val
        part1 += get_hash(step)
    return part1, get_focusing_power(boxes)
    
def get_focusing_power(boxes_config: dict):
    ret = 0
    for box_num in boxes_config:
        for slot_num, (lens_id, lens_length) in enu(boxes_config[box_num].items(), 1):
            ret += (box_num + 1) * slot_num * lens_length
    return ret


def get_hash(s):
    current_value = 0
    for letter in s:
        current_value += ord(letter)
        current_value *= 17
        current_value %= 256
    return current_value


samp = r"""
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

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