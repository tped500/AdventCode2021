
file = open("input_example.txt", "r")
input_list = [line.rstrip() for line in file.readlines()]

epsilon_rate = 0
len_input = len(input_list)

# criar lista inicial com resultado de winners
initial_sum = 0
initial_list_winners = []
initial_list_losers = []

def calculate_winner(input):
    counter_sum = 0
    # for element in input:
    #      counter_sum += int(element)
    if sum(input) > len(input)/2:
        return 1
    else:
        return 0

print("Mein Spatz I love you ")
#print(calculate_winner([0, 1, 1, 0, 1]))

# Calculate number of rows
rows_length = len(list(input_list[0:]))
print(rows_length)
column = 0
new_list = []
while column < rows_length:
    new_list.append(list(input_list[column][0]))
    #print(new_list)
    #print(calculate_winner(list(input_list[column[0]])))


    #    sum_of_column = calculate_winner(input_list[int(column)])
    column += 1
    # for element in input_list:
    #     sum_of_column += int(element[column]) # iterar aqui para ver que elementos ficam
    # column += 1
    #
    # if sum_of_column > len_input / 2:
    #     gamma_final.append(1)
    # else:
    #     gamma_final.append(0)
    #

# for prev_winner in gamma_final:
#     winner_list = [element for element in input_list if element.startswith(str(gamma_final[winner_col]))]
#     loser_list = [element for element in input_list if element.startswith(str(abs(gamma_final[winner_col])-1))]




#
# # Calculate decimal number from binary
# num = 0
# num_epsilon = 0
# for b in gamma_final:
#     num = 2 * num + b
#     num_epsilon = 2 * num_epsilon + (0 if b == 1 else 1)
#
# power_consumption = num * num_epsilon
# print(power_consumption)
#



# # life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
# o2 = 0
# co2 = 0
