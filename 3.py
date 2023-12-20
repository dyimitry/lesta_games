m = [16, 19, 2, 12,16, 16, 20, 15, 20, 15]


def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = list(filter(lambda x: x == elem, s))
    right = [x for x in s if x > elem]
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort(m))


"""
В алгоритме быстрой сортировки мы сначала хитрым способом разделим данные на части, зато объединение произойдёт очень
 просто, нам достаточно будет дописать один отсортированный массив после другого.Сложность быстрой сортировки в среднем 
 — такая же, как в лучшем случае: O(n*log(n)).
"""