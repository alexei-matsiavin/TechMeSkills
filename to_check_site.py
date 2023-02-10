#Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, только для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу.

#Напишите программу, которая запрашивает у клиента, сколько будет сайтов, а затем запрашивает название продукта и после каждого запроса выводит на экран активные сайты.

#Условия: структуру сайта нужно описать один раз, копипасту никто не любит.

#Подсказка: используйте рекурсию.

import copy


# def new_site(dictionary, number, list_site):
#     for i in range(number):
#         name = input('Введите название продукта для нового сайта: ')
#         list_site[i][0] = name
#         list_site[i][1] = copy.deepcopy(dictionary)
#         list_site[i][1]['html']['head']['title'] = 'Куплю/продам {phone} недорого'.format(phone=name)
#         list_site[i][1]['html']['body']['h2'] = 'У нас самая низкая цена на {phone}'.format(phone=name)
#         printer(list_site, i+1)

def new_site(dictionary, number, list_site_f, i=0):
    if number > 0:
        name = input('Введите название продукта для нового сайта: ')
        list_site_f[i][0] = name
        list_site_f[i][1] = copy.deepcopy(dictionary)
        list_site_f[i][1]['html']['head']['title'] = 'Куплю/продам {phone} недорого'.format(phone=name)
        list_site_f[i][1]['html']['body']['h2'] = 'У нас самая низкая цена на {phone}'.format(phone=name)
        printer(list_site_f, i + 1)
        i += 1
        new_site(dictionary, number - 1, list_site_f, i)


def printer(list_site_p, num):
    number = 0
    for i in list_site_p:
        if number < num:
            print(f'Сайт для {i[0]}:')
            print(f'{i[1]}')
            number += 1
        else:
            break


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {phone} недорого'  # .format(phone = name)
        },
        'body': {
            'h2': 'У нас самая низкая цена на {phone}',  # .format(phone = name),
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

site_number = int(input('Сколько сайтов: '))
list_site = [['', ''] for i in range(site_number)]
new_site(site, site_number, list_site)