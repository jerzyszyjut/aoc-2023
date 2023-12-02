lines: list[str] = []

with open("1/calibration_values_2.txt", "r") as file:
  lines = file.readlines()

sum_of_codes: int = 0

numbers_representations: tuple[tuple[str, str]] = (
  ("one", "1"),
  ("two", "2"),
  ("three", "3"),
  ("four", "4"),
  ("five", "5"),
  ("six", "6"),
  ("seven", "7"),
  ("eight", "8"),
  ("nine", "9"),
  ("zero", "0"),
)

lines_with_replaced_numbers: list[str] = []

for line in lines:
  replaced_line: str = ""
  for index in range(len(line)):
    for number_representation in numbers_representations:
      if line[index:].startswith(number_representation[0]):
        replaced_line += number_representation[1]
        index += len(number_representation[0])
      else:
        replaced_line += line[index]
  lines_with_replaced_numbers.append(replaced_line)

for line in lines_with_replaced_numbers:
  first_number: str = None
  last_number: str = None

  for character in line:
    if character.isnumeric():
      if first_number == None:
        first_number = character
      last_number = character

  line_code: int = int(first_number + last_number)
  sum_of_codes += line_code
    
print(sum_of_codes)
