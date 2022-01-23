
file = open("input_example.txt", "r")
input_list = [line.rstrip() for line in file.readlines()]

epsilon_rate = 0
len_input = len(input_list)

gamma_final = []
column = 0

while column < len(input_list[0]):
    sum_of_column = 0
    # Calculate the more/less common
    for element in input_list:
        sum_of_column += int(element[column]) # iterar aqui para ver que elementos ficam
    column += 1

    if sum_of_column > len_input / 2:
        gamma_final.append(1)
    else:
        gamma_final.append(0)


winner_col = 0
winner_list = []
loser_list = []
# usar uma list comprehension para tirar todos os valores que comecam com cada elemento de gamma_final
# Setting up the initial array with winners and losers
for prev_winner in gamma_final:
    winner_list = [element for element in input_list if element.startswith(str(gamma_final[winner_col]))]
    loser_list = [element for element in input_list if element.startswith(str(abs(gamma_final[winner_col])-1))]

# Check if we are the end of the winner's list
while len(winner_list) != 1:





print("Winners: ", winner_list)
print("Losers: ", loser_list)
#
#
#
# while winner_col < len(input_list[0]):
#     for candidate in input_list:
#         if not winner_list:  # if winner_list is empty (start of check)
#             if int(candidate[0]) == int(gamma_final[winner_col]):
#                 winner_list.append(candidate)
#             else:
#                 loser_list.append(candidate)
#         else:
#             if int(candidate[0]) == int(gamma_final[winner_col]):
#                 winner_list.append(candidate)
#             else:
#                 loser_list.append(candidate)
#     winner_col += 1
# #print(winner_list)
#
# print("Winners: ", winner_list)
# print("Losers: ", loser_list)




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
