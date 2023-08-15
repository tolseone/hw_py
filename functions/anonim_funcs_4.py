# <название штата>: <численность населения>
# Vermont: 626299
# Massachusetts: 7029917
data = [
    (19542209, 'New York'), (4887871, 'Alabama'),
    (1420491, 'Hawaii'), (626299, 'Vermont'),
    (1805832, 'West Virginia'), (39865590, 'California'),
    (11799448, 'Ohio'), (10711908, 'Georgia'), 
    (10077331, 'Michigan'), (10439388, 'Virginia'), 
    (7705281, 'Washington'), (7151502, 'Arizona'), 
    (7029917, 'Massachusetts'), (6910840, 'Tennessee')
    ]
# new_data = sorted(data, reverse = True, key = lambda info: info[1][-1])
# print(*list(map(lambda info: f"{info[1]}: {info[0]}", new_data)), sep='\n')

print(*list(map(lambda info: f"{info[1]}: {info[0]}", sorted(data, reverse = True, key = lambda info: info[1][-1]))), sep='\n')
