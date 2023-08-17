# 3.1
# total_summ = 0
#
# cond_grass = str(input('Добрый день, есть ли у Вас газон? '))
# if (cond_grass.strip()).lower() == 'да':
#     sqr_grass = int(input('Какова его площадь (сотки)? '))
#     total_summ += 2 * sqr_grass
#
# cond_deciduous_tree = str(input('Есть ли у вас Лиственные деревья? '))
# if (cond_deciduous_tree.strip()).lower() == 'да':
#     num_deciduous_tree = int(input('Сколько? '))
#     total_summ += 20 * num_deciduous_tree
#
# cond_conifer_tree = str(input('Есть ли у вас Хвойные деревья? '))
# if (cond_conifer_tree.strip()).lower() == 'да':
#     num_conifer_tree = int(input('Сколько? '))
#     total_summ += 8 * num_conifer_tree
#
# cond_pool = str(input('Есть ли водоем? '))
# if (cond_pool.strip()).lower() == 'да':
#     num_pool = int(input('Каков его объем (Кубометры)? '))
#     if num_pool < 20:
#         total_summ += 6 * num_pool + 60
#     else:
#         total_summ += 4 * num_pool + 60
#
# if (cond_grass.strip()).lower() or (cond_deciduous_tree.strip()).lower() or (cond_conifer_tree.strip()).lower() or \
#         (cond_pool.strip()).lower() == 'да':
#     total_summ += 10
#
# print(f'наши услуги будут стоить:{total_summ}$')

# 3.2
# HEIGHT = 3000
# WIRE_WEIGHT = {3: 0.056, 4: 0.099, 5: 0.154, 2: 0.0247, 1: 0.0062}
#
# length = input("Enter length")
# if length.endswith('mm'):
#     l_multiplier = 1
#     length = int(length[:-2].strip())
# elif length.endswith('cm'):
#     l_multiplier = 10
#     length = int(length[:-2].strip())
# else:
#     l_multiplier = 1000
#     length = int(length[:-1].strip())
#
# mesh_edge = input("Enter mesh cell size")
# if mesh_edge.endswith('mm'):
#     m_multiplier = 1
#     mesh_edge = int(mesh_edge[:-2].strip())
# elif mesh_edge.endswith('cm'):
#     m_multiplier = 10
#     mesh_edge = int(mesh_edge[:-2].strip())
# else:
#     m_multiplier = 1000
#     mesh_edge = int(mesh_edge[:-1].strip())
#
# length_mm = length * l_multiplier
# mesh_edge_mm = mesh_edge * m_multiplier
#
# wire_diametr = int(input('Enter wire diametr'))
#
# wire_length = 2 * length_mm / mesh_edge_mm * HEIGHT * 2 / 3 ** 0.5
# wire_length_m = wire_length / 1000
#
# print(
#     f'You need {round(wire_length_m * WIRE_WEIGHT[wire_diametr],3)} kg of '
#     f'wire {wire_diametr} mm in diametr'
# )

# 3.3
# num = 6
# store = []
# STRATEGY = str(input('Выберите стратегию(LIFO/FIFO)? '))
# if STRATEGY.upper() == 'LIFO':
#     while num > 0:
#         item = str(input('Что у вас? '))
#         if item.isalpha():
#             print('Спасибо')
#             store.append(item)
#         else:
#             if len(store) == 0:
#                 print('Дружеские подбадривания')
#             else:
#                 print(f'Вот вам {store.pop()}')
#         num -= 1
# elif STRATEGY.upper() == 'FIFO':
#     while num > 0:
#         item = str(input('Что у вас? '))
#         if item.isalpha():
#             print('Спасибо')
#             store.append(item)
#         else:
#             if len(store) == 0:
#                 print('Дружеские подбадривания')
#             else:
#                 print(f'Вот вам {store[0]}')
#                 del store[0]
#         num -= 1


# num = 6
# store = []
# STRATEGY = str(input('Выберите стратегию(LIFO/FIFO)? '))
# while STRATEGY.upper() !='LIFO' and STRATEGY.upper() !='FIFO':
#     STRATEGY = str(input('Выберите стратегию(LIFO/FIFO)? '))
# else:
#     while num > 0:
#         item = str(input('Что у вас? '))
#         if item.isalpha():
#             print('Спасибо')
#             store.append(item)
#         else:
#             if len(store) == 0:
#                 print('Дружеские подбадривания')
#             else:
#                 if STRATEGY.upper() !='LIFO':
#                     print(f'Вот вам {store.pop()}')
#                 else:
#                     print(f'Вот вам {store[0]}')
#                     del store[0]
#         num -= 1

# 3.4
# REALTY = [
#     {'price': 23000, 'area': 2200, 'internet': True, 'electricity': True, 'booked': True},
#     {'price': 12200, 'area': 1200, 'internet': True, 'electricity': True, 'booked': False},
#     {'price': 22300, 'area': 2120, 'internet': False, 'electricity': True, 'booked': True},
#     {'price': 15000, 'area': 1600, 'internet': True, 'electricity': False, 'booked': False},
#     {'price': 25400, 'area': 2600, 'internet': False, 'electricity': True, 'booked': False},
#     {'price': 16000, 'area': 1700, 'internet': True, 'electricity': False, 'booked': False},
#     {'price': 34000, 'area': 3600, 'internet': True, 'electricity': True, 'booked': False},
#     {'price': 23000, 'area': 2050, 'internet': True, 'electricity': True, 'booked': True},
#     {'price': 45000, 'area': 3800, 'internet': False, 'electricity': True, 'booked': False},
#     {'price': 23000, 'area': 2150, 'internet': True, 'electricity': False, 'booked': True},
#     {'price': 67000, 'area': 4850, 'internet': True, 'electricity': True, 'booked': True},
#     {'price': 32300, 'area': 2820, 'internet': False, 'electricity': True, 'booked': True},
#     {'price': 19700, 'area': 1800, 'internet': True, 'electricity': False, 'booked': False},
#     {'price': 12300, 'area': 1050, 'internet': False, 'electricity': True, 'booked': True},
#     {'price': 45700, 'area': 4270, 'internet': True, 'electricity': True, 'booked': False},
# ]

# need_area = int(input('Добрый день, участок какой площади вам необходим? '))
# min_price = 99999
# cur_area = ''
# for area in REALTY:
#     if area['area'] > need_area and min_price > area['price'] and area['booked'] is False:
#         min_price = area['price']
#         cur_area = area['area']
# if min_price == 99999:
#     print('К сожалению, нет свободных участков такой площади')
# else:
#     print(f'Самое дешевое предложение {min_price}, площадь участка {cur_area}')
#
#
# result = 0
# max_square, res_square = 0, 0
# start_pos, end_pos, summ = 0, 0, 0
# for num in range(0, len(REALTY)):
#     a = REALTY[num]
#     if REALTY[num]['booked'] == False:
#         max_square += REALTY[num]['area']
#         summ += 1
#     else:
#         if res_square < max_square:
#             res_square = max_square
#             end_pos = num
#             start_pos = num - summ
#             summ = 0
#         max_square = 0
# print(f'Добрый день, наибольший возможный участок {res_square} (можно купить участки {start_pos}-{end_pos-1})')

num = 6
store = []
STRATEGY = str(input('Выберите стратегию(LIFO/FIFO)? '))
while STRATEGY.upper() != 'LIFO' and STRATEGY.upper() != 'FIFO':
    STRATEGY = str(input('Выберите стратегию(LIFO/FIFO)? '))
else:
    while num > 0:
        item = str(input('Что у вас? '))
        if num == 6:
            store.append({'name': item, 'amount': 0})
        if item:
            amount = int(input('Сколько?'))
            for _ in range(len(store)):
                if store[_]['name'] == item:
                    store[_]['amount'] += amount
                else:
                    store.append({'name': item, 'amount': amount})
            print('Спасибо')
        else:
            if len(store) == 0:
                print('Дружеские подбадривания')
            else:
                if STRATEGY.upper() != 'LIFO':
                    print(f'Вот вам {store[len(store)-1]["name"]}')

                    store[len(store) - 1]["amount"] -= 1
                else:
                    print(f'Вот вам {store[0]["name"]}')
                    store[0]["amount"] -= 1
        for _ in range(len(store)):
            if store[_]['amount'] == 0:
                del store[_]
        num -= 1
