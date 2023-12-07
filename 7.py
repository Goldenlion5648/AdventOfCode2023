from AoCLibrary import *
with open("input7.txt") as f:
    real_input = f.read()

def main(a : str):
    a = a.strip()
    inp = AdventInput(data=a)
    ret = 0
    Hand = namedtuple('Hand', ['cards', 'bid'])
    cards = []
    for full_hand in inp.lines:
        hand, value = full_hand.split() 
        cards.append(Hand(hand, int(value)))

    return get_total_winnings(cards, get_hand_value), get_total_winnings(cards, get_hand_value_part2)

    


JOKER = "J"
    
def get_best_type_with_joker(hand: str):
    if JOKER not in hand:
        return get_type(hand)
    
    card_faces = "AKQT98765432J"
    
    return min(
        get_type(hand.replace(JOKER, swap_value))
        for swap_value in card_faces
    )

def get_hand_value(hand):
    return (get_type(hand),) + get_tie_breaker(hand)

def get_hand_value_part2(hand):
    return (get_best_type_with_joker(hand),) + get_tie_breaker_part2(hand)

def get_total_winnings(cards: list, function=get_hand_value):
    cards.sort(key=lambda x: function(x[0]))
    cards.reverse()
    # printe(cards)
    return sum(i * value for i, (hand, value) in enu(cards, 1))


def get_tie_breaker(hand):
    card_strengths = "AKQJT98765432"
    return tuple(card_strengths.index(x) for x in hand)
    

def get_tie_breaker_part2(hand: str):
    card_strengths2 = "AKQT98765432J"
    return tuple(card_strengths2.index(x) for x in hand)


def get_type(hand):
    kinds = Counter(hand)
    if 5 in kinds.values():
        return 5
    if 4 in kinds.values():
        return 6
    if 3 in kinds.values() and 2 in kinds.values():
        return 7
    if 3 in kinds.values():
        return 8
    current_counts = list(kinds.values())
    if current_counts.count(2) == 2:
        return 9
    if current_counts.count(2) == 1:
        return 10
    if len(kinds.values()) == 5:
        return 11
    return 12
    



samp = r"""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

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