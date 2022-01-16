file = open("input_raw.txt", "r")
input_list = [line.rstrip() for line in file.readlines()]

epsilon_rate = 0
len_input = len(input_list)

gamma_final = []
column = 0

while column < len(input_list[0]):
    sum_of_column = 0
    for element in input_list:
        sum_of_column += int(element[column])
    column += 1

    if sum_of_column > len_input / 2:
        gamma_final.append(1)
    else:
        gamma_final.append(0)


num = 0
num_epsilon = 0
for b in gamma_final:
    num = 2 * num + b
    num_epsilon = 2 * num_epsilon + (0 if b == 1 else 1)

power_consumption = num * num_epsilon
print(power_consumption)


