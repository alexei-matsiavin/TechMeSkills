import random

flesh = '0OoQD'
SIZE = 5
veggies = 'Il1'
SKEWER = '==~-{}---'
people = 3  # int(input('How many of you are there? '))
total = ''
while total.count('==') < people:
    bits = ''
    while len(bits) < SIZE * 2:
        bits += f'{random.choice(flesh)}{random.choice(veggies)}'
    bits += random.choice(flesh)
    total += "\n |%14s\n" % "|" + (SKEWER.format(bits))
total += "\n |%14s\n" % "|"
print(total)

# max_lenth = len(total)
# num = 0
# for position_kebab in range(18, max_lenth, 36):
#     num += 1
#     free_place = 0
#     kebab = total[position_kebab: position_kebab + 18]
#     for ingredient in kebab:
#         if ingredient == '-':
#             free_place += 1
#     if free_place > 4:
#         print(f'Шашлык номер - {num} : {kebab} - шампур недогружен')
#     elif free_place < 4:
#         print(f'Шашлык номер - {num} : {kebab} - шампур перегружен')
#     else:
#         print(f'Шашлык номер - {num} : {kebab} - отличный шашлык можно жарить')
grill_dict = {}


def grill_width(photo_grill):
    num_pos = 0
    pos_list = []
    for pos, letter in enumerate(photo_grill):
        if letter == '|':
            num_pos += 1
            pos_list.append(pos)
        if num_pos == 2:
            return pos_list[1] - pos_list[0]


# print(grill_width(total))


def check_grill(photo_grill, grill_width_f=14):
    max_length = len(photo_grill)
    len_skewer = grill_width_f + 4
    num = 0
    for position_kebab in range(len_skewer, max_length, len_skewer * 2):
        num += 1
        free_place = 0
        kebab = total[position_kebab: position_kebab + 18]
        for ingredient in kebab:
            if ingredient == '-':
                free_place += 1
        grill_dict[num] = kebab
        if free_place > 4:
            print(f'Шашлык номер - {num} : {kebab} - шампур недогружен')
        elif free_place < 4:
            print(f'Шашлык номер - {num} : {kebab} - шампур перегружен')
        else:
            print(f'Шашлык номер - {num} : {kebab} - отличный шашлык можно жарить')


check_grill(total)
print(grill_dict)
