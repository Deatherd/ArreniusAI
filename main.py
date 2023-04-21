# set_string = input()
# get_string = input()
# p = float(input())


def pascal_triangle(rows):
    row = [1]
    for i in range(rows):
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return row


def get_probability(fork_count, position, p):
    coeff = pascal_triangle(fork_count)
    if (fork_count + position) % 2:
        return coeff[] * p ** (...) * (1 - p) ** (...)
    else:
        return 0


set_string = 'rlrlr'
get_string = 'rll?r'
p = 0.40

target = 0
offset = 0

inc = {'l': -1, 'r': 1}
for char in set_string:
    target += inc.get(char, 0)

for char in get_string:
    offset += inc.get(char, 0)

# ## Ключ - место,итем - вероятность
# destinations = {0: 1}
# intercept = 0
# for char in get_string:
#     incr = inc.get(char, 0)
#     if char == '?':
#         new_destinations = destinations
#         for key, item in destinations.items():
#             new_destinations[key - 1] += item * p
#             new_destinations[key + 1] += item * (1 - p)
#         destinations = new_destinations
#     else:
#         intercept += incr
#
#
# # print('Возможные положения:')
# # for key, item in destinations.items():
# #     print(f'Для координаты {key} вероятность {item}')
#
# print(destinations.get(target-intercept, 0))
