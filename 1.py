# 1 способ
tuple_even = (-8, -6, -4, -2, 0, 2, 4, 6, 8)


def func(value: int):
    str_value = str(value)
    last_number = int(str_value[-1])
    if last_number in tuple_even:
        return True
    return False


print(func(int(input())))

# 2 способ наиболее быстрый: Алгоритм побитового сравнения
integer = 119
binary = format(integer, 'b')


def funck_even(integer):
    if integer & 1 == 0:
        return True
    return False


print(funck_even(integer))
