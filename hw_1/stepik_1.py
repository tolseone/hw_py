sum = 0
with open('prices.txt', 'r', encoding='utf-8') as file:
    for line in file:
        list = line.split()
        sum += int(list[1]) * int(list[2])
    print(sum)