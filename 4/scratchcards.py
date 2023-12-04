lines: list[str] = []

with open("4/cards_1.txt") as f:
    lines = f.read().split("\n")

# Part 1

points: list[int] = []
for line in lines:
    card_id: int = int(line.split("Card ")[1].split(":")[0])
    numbers: str = line.split(": ")[1]
    winning_numbers: list[int] = list(map(int, list(filter(lambda x: len(x)>0, numbers.split(" | ")[0].split(" "))) ))
    player_numbers: list[int] = list(map(int, list(filter(lambda x: len(x)>0, numbers.split(" | ")[1].split(" "))) ))
    hit_numbers: int = len(list(filter(lambda x: x in winning_numbers, player_numbers)))
    if hit_numbers > 0:
        points.append(1 << (hit_numbers-1))
    else:
        points.append(0)
    
print(sum(points)) 

# Part 2

with open("4/cards_2.txt") as f:
    lines = f.read().split("\n")

copies: dict[int, int] = {}

for line in lines:
    card_id: int = int(line.split("Card ")[1].split(":")[0])
    numbers: str = line.split(": ")[1]
    winning_numbers: list[int] = list(map(int, list(filter(lambda x: len(x)>0, numbers.split(" | ")[0].split(" "))) ))
    player_numbers: list[int] = list(map(int, list(filter(lambda x: len(x)>0, numbers.split(" | ")[1].split(" "))) ))
    hit_numbers: int = len(list(filter(lambda x: x in winning_numbers, player_numbers)))
    owned_cards: int = copies.get(card_id, 1)
    for i in range(1, hit_numbers+1):
        copies[card_id+i] = copies.get(card_id+i, 1) + owned_cards
    copies[card_id] = owned_cards
    
print(sum(copies.values()))
