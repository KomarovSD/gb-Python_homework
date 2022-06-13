#Задача №5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных
# из трех случайных слов, взятых из трёх списков (по одному из каждого)

from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом", ]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    """Функция возвращает случайные шутки, собранные из трех спискоd"""

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if flag:
            jokes.append(f'{no.pop(num)} {adv.pop(num)} {adj.pop(num)}')
        else:
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return jokes


print(get_jokes(3, flag=True))
