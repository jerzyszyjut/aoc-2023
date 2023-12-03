lines: list[list[str]] = []

with open("3/engine_schema_1.txt", "r") as file:
    lines = file.read().split("\n")

# Part 1
numbers: list[list[int]] = []

for i in range(len(lines)):
    is_in_number: bool = False
    is_number_adjacent_to_symbol: bool = False
    current_number: str = ""
    
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            current_number += lines[i][j]
            is_in_number = True
            
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i + k >= 0 and i + k < len(lines) and j + l >= 0 and j + l < len(lines[i]):
                        checked_char: str = lines[i + k][j + l]
                        if not checked_char.isnumeric() and checked_char != ".":
                            is_number_adjacent_to_symbol = True
        else:
            if is_in_number:
                if is_number_adjacent_to_symbol:
                    numbers.append(int(current_number))
                is_in_number = False
                is_number_adjacent_to_symbol = False
                current_number = ""
                
        if j == len(lines[i]) - 1 and is_in_number and is_number_adjacent_to_symbol:
            numbers.append(int(current_number))
            
print(sum(numbers))

# Part 2
lines: list[list[str]] = []

with open("3/engine_schema_2.txt", "r") as file:
    lines = file.read().split("\n")

gears: dict[tuple[int, int], set[int]] = {}

for i in range(len(lines)):
    is_in_number: bool = False
    is_number_adjacent_to_gear_symbol: bool = False
    gear_symbol_positions: list[tuple[int, int]] = []
    current_number: str = ""
    
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            current_number += lines[i][j]
            is_in_number = True
            
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i + k >= 0 and i + k < len(lines) and j + l >= 0 and j + l < len(lines[i]):
                        checked_char: str = lines[i + k][j + l]
                        if checked_char == "*":
                            is_number_adjacent_to_gear_symbol = True
                            gear_symbol_positions.append((i + k, j + l))
        else:
            if is_in_number:
                if is_number_adjacent_to_gear_symbol:
                    for pos in gear_symbol_positions:
                        position_string: str = str(pos[0]) + "," + str(pos[1])
                        if position_string in gears:
                            gears[position_string].add(int(current_number))
                        else:
                            gears[position_string] = set([int(current_number)])
                is_in_number = False
                is_number_adjacent_to_gear_symbol = False
                gear_symbol_positions = []
                current_number = ""
                
        if j == len(lines[i]) - 1 and is_in_number and is_number_adjacent_to_gear_symbol:
            for pos in gear_symbol_positions:
                position_string: str = str(pos[0]) + "," + str(pos[1])
                if position_string in gears:
                    gears[position_string].add(int(current_number))
                else:
                    gears[position_string] = set([int(current_number)])
                
correct_gears: list[int] = []

for numbers in gears.values():
    if len(numbers) == 2:
        correct_gears.append(numbers.pop() * numbers.pop())
        
print(sum(correct_gears))
