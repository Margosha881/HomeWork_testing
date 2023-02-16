geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def search_visit_ru():
    vizit_all = []
    for vizit_ru in geo_logs:
        for vizits, [Sity, Country] in vizit_ru.items():
            if Country == 'Россия':
                vizit_all.append(vizit_ru)
    return vizit_all


def search_uniq_id():
    geo_id = ids.values()
    uniq_id = set()
    for value in geo_id:
        for id in value:
            uniq_id.add(id)
    return list(uniq_id)


def search_max_sales_amount():
    max_stat = max(stats, key=stats.get)
    amount = max_stat, stats[max_stat]
    return amount



# print(search_visit_ru(geo_logs))
# print()
# print(search_uniq_id(ids))
# print(search_max_sales_amount(stats))