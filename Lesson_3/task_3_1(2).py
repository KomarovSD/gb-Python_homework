# Задача №1(2).
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c англ. на рус.
# Если перевод сделать невозможно, вернуть None.
# Вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
# — результат тоже должен быть с заглавной.

DICT_NUM = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "Ten": "десять"
}


# .1
def num_translate(num_word):
    """Функция конвертиркует one to  один ... ten to десять"""
    return DICT_NUM.get(num_word)


# .2
def num_translate_adv(num_word):
    """ Функция конвертиркует one to  один ... ten to десять, с заглавной буквы """
    value = DICT_NUM.get(num_word.lower())

    if value:
        return value.capitalize() \
            if num_word[0].isupper() \
            else value

    return None


# Check
print(num_translate('one'))
print(num_translate('Ten'))
print(num_translate('eleven'))
print(f"{'':-^80}")
print(num_translate_adv('One'))
print(num_translate_adv('eight'))
