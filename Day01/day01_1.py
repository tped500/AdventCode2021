f = open("input_raw.txt", "r")

lines_file = [int(line) for line in f.readlines()]
len_file = len(lines_file)
iterator = 0
counter = 0

while iterator < len_file-1:
    if lines_file[iterator] < lines_file[iterator + 1]:
        counter += 1
    iterator += 1

print(counter)