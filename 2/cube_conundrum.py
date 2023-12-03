lines: list[str] = []

with open("2/game_1.txt", "r") as file:
  lines = file.readlines()
  
lines = [line.strip() for line in lines]

cube_amounts: dict[str, int] = {
  "red": 12,
  "green": 13,
  "blue": 14,
}

sum_of_possible_games: int = 0
sum_of_powers_of_minimum_cube_amount: int = 0

for line in lines:
  game_id: int = int(line.split("Game ")[1].split(":")[0])
  game_possible: bool = True
  draws: list[str] = line.split(": ")[1].split("; ")
  minimum_cube_amounts: dict[str, int] = {
    "red": 0,
    "green": 0,
    "blue": 0,
  }
  for draw in draws:
    cubes = draw.split(", ")
    for cube in cubes:
      cubes_number: int = int(cube.split(" ")[0])
      cubes_color: str = cube.split(" ")[1]
      if cubes_number > cube_amounts[cubes_color]:
        game_possible = False
      minimum_cube_amounts[cubes_color] = max(minimum_cube_amounts[cubes_color], cubes_number)
  if game_possible:
    sum_of_possible_games += game_id
  sum_of_powers_of_minimum_cube_amount += minimum_cube_amounts["red"] * minimum_cube_amounts["green"] * minimum_cube_amounts["blue"]

print(sum_of_powers_of_minimum_cube_amount)
