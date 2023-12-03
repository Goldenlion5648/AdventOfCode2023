from AoCLibrary import *
with open("input3.txt") as f:
    real_input = f.read()

used = set()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    board = to_board(a)    
    def part1():
        used.clear()
        ret = 0
        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x].isdigit() :
                    if any(
                            board[y + dy][x + dx] not in ".0987654321" for dy, dx in adj8
                            if y + dy in range(len(board)) and 
                            x + dx in range(len(board[0]))
                    ):
                        cur =  expand(board, y, x)
                        ret += cur
        return ret
        
    def part2():
        used.clear()
        ret = 0
        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x] == '*':
                    mult = 1
                    seen = 0
                    for dy, dx in adj8:
                        temp = expand(board, dy + y, x + dx)
                        if temp != 0:
                            mult *= temp
                            seen += 1
                    if seen == 2:
                        ret += mult
        return ret
    
    return part1(), part2()

def expand(board, y, x):
    i = 0
    ret = ''
    if board[y][x] =='.':
        return 0
    while x -i >= 0 and board[y][x-i].isdigit() :
        cur = (y, x - i)
        if cur in used: 
            return 0
        ret = board[y][x-i] + ret
        used.add(cur)
        i += 1
    i = 1
    while x+i < len(board[y]) and board[y][x+i].isdigit():
        cur = (y, x + i)
        if cur in used: 
            return 0
        ret += board[y][x+i]
        i += 1
    return int(ret)




samp = r"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

""".lstrip("\n")

sample_answer = main(samp)
print("sample", sample_answer)

result = main(real_input)
ans(result)