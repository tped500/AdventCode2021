file = open("input_example.txt", "r")

depth = 0
horizontal = 0
aim = 0

input_file = [line.rstrip() for line in file.readlines()]

"""
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
"""

for command in input_file:
    split = command.split(" ")
    type_position = split[0]
    position_shift = split[1]
    if type_position == "forward":
        horizontal += int(position_shift)
        depth = int(aim)*int(position_shift)
    elif type_position == "down":
        depth += int(position_shift)
        aim += int(position_shift)
    else:
        depth -= int(position_shift)
        depth -= int(position_shift)

print(depth)
print(horizontal)
print(depth*horizontal)