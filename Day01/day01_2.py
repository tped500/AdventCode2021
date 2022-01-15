f = open("input_raw.txt", "r")

lines_file = [int(line) for line in f.readlines()]
len_file = len(lines_file)
iterator = 2
new_array = []

while iterator < len_file:
    new_array.append(sum(lines_file[iterator-2:iterator+1]))
    iterator += 1

new_array_i = 0
counter = 0
while new_array_i < len(new_array) - 1:
    if new_array[new_array_i] < new_array[new_array_i + 1]:
        counter += 1
    new_array_i += 1

print(counter)