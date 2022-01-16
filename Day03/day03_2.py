
file = open("input_example.txt", "r")
input_list = [line.rstrip() for line in file.readlines()]

epsilon_rate = 0
len_input = len(input_list)

gamma_final = []
column = 0
winner_list = []


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


winner_list = []
loser_list = []
winner_col = 0
while winner_col < len(input_list[0]):
    for candidate in input_list:
        #print(gamma_final[winner_col])
        if int(candidate[0]) == int(gamma_final[winner_col]):
            winner_list.append(candidate)
        else:
            loser_list.append(candidate)
            #print(candidate)
    winner_col += 1
#print(winner_list)

print("Winners: ", winner_list)
print("Losers: ", loser_list)




# Go through gamma_final to evaluate most common elements
# Take each common element and extract all those who win
winner_list = []
new_position = 0
for candidate in gamma_final:
    for element in input_list:
        if element[0] == candidate:
            winner_list.append(element)
        new_position += 1



# calcular o mais/menos comum
# guardar num array as linhas que obedecem a regra

# Calculate decimal number from binary
num = 0
num_epsilon = 0
for b in gamma_final:
    num = 2 * num + b
    num_epsilon = 2 * num_epsilon + (0 if b == 1 else 1)

power_consumption = num * num_epsilon
print(power_consumption)

# life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
o2 = 0
co2 = 0
