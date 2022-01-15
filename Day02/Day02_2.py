file = open("input_raw.txt", "r")

depth = 0
horizontal = 0
aim = 0

input_file = [line.rstrip() for line in file.readlines()]


for command in input_file:
    split = command.split(" ")
    type_position = split[0]
    position_shift = split[1]
    if type_position == "forward":
        horizontal += int(position_shift)
        depth += (int(aim)*int(position_shift))
    elif type_position == "down":
        aim += int(position_shift)
    else:
        aim -= int(position_shift)


print(aim)
print(depth)
print(horizontal)
print(depth*horizontal)