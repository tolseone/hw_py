with open('line.txt', 'r', encoding = 'utf - 8') as file:
    content = [line for line in file]
    maximum = 0
    for elem in content:
        if len(elem) > maximum:
            maximum = len(elem)
    print(*[line for line in content if len(line) == maximum], sep='\n')
