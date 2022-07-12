

def odd_num(n):
    """Генератор нечётных чисел от 1 до n, используя ключевое слово yield"""
    for i in range(1, n + 1, 2):
        yield i


def odd_num_no_yield(n):
    """Генератор нечётных чисел от 1 до n, не используя ключевое слово yield"""
    return (x for x in range(1, n + 1, 2))


if __name__ == "__main__":
    a_gen = odd_num(15)
    b_gen = odd_num_no_yield(15)

    print("a_gen type", type(a_gen))
    print("b_gen type", type(b_gen))

    for val in a_gen:
        print(val)

    print(f"{a_gen}")

